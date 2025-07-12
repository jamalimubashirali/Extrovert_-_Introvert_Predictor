import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Page configuration
st.set_page_config(
    page_title="Personality Predictor",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .prediction-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_and_prepare_data():
    """Load and prepare the training data"""
    try:
        df = pd.read_csv('Data/train.csv', index_col='id')
        
        # Fill missing values in categorical columns
        for col in ['Stage_fear', 'Drained_after_socializing']:
            mode_value = df[col].mode()[0]
            df[col].fillna(mode_value, inplace=True)
        
        # Convert categorical to numerical
        df['Drained_after_socializing'] = df['Drained_after_socializing'].map({'Yes': 1, 'No': 0})
        df['Stage_fear'] = df['Stage_fear'].map({'Yes': 1, 'No': 0})
        df['Personality'] = df['Personality'].map({'Extrovert': 0, 'Introvert': 1})
        
        # Impute missing values in numerical columns
        imputer = SimpleImputer(strategy='mean')
        cols_to_impute = df.drop(columns=['Stage_fear', 'Drained_after_socializing', 'Personality'], axis=1).columns
        df[cols_to_impute] = imputer.fit_transform(df[cols_to_impute])
        
        return df, imputer
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

@st.cache_resource
def train_model(df):
    """Train the logistic regression model"""
    X = df.drop(columns=['Personality'])
    y = df['Personality']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    
    # Calculate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy

def create_input_form():
    """Create the input form for user data"""
    st.markdown("### 📊 Enter Your Characteristics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Time & Social Behavior**")
        time_spent_alone = st.slider(
            "Hours spent alone per day", 
            min_value=0.0, 
            max_value=12.0, 
            value=3.0, 
            step=0.5
        )
        
        social_event_attendance = st.slider(
            "Social events attended per month", 
            min_value=0, 
            max_value=10, 
            value=5, 
            step=1
        )
        
        going_outside = st.slider(
            "Times going outside per week", 
            min_value=0, 
            max_value=7, 
            value=4, 
            step=1
        )
        
        friends_circle_size = st.slider(
            "Number of close friends", 
            min_value=0, 
            max_value=20, 
            value=8, 
            step=1
        )
        
        post_frequency = st.slider(
            "Social media posts per week", 
            min_value=0, 
            max_value=15, 
            value=5, 
            step=1
        )
    
    with col2:
        st.markdown("**Psychological Traits**")
        stage_fear = st.selectbox(
            "Do you experience stage fear?",
            options=['No', 'Yes']
        )
        
        drained_after_socializing = st.selectbox(
            "Do you feel drained after socializing?",
            options=['No', 'Yes']
        )
    
    return {
        'Time_spent_Alone': time_spent_alone,
        'Stage_fear': stage_fear,
        'Social_event_attendance': social_event_attendance,
        'Going_outside': going_outside,
        'Drained_after_socializing': drained_after_socializing,
        'Friends_circle_size': friends_circle_size,
        'Post_frequency': post_frequency
    }

def predict_personality(model, user_data):
    """Make personality prediction"""
    # Convert categorical variables
    user_data['Stage_fear'] = 1 if user_data['Stage_fear'] == 'Yes' else 0
    user_data['Drained_after_socializing'] = 1 if user_data['Drained_after_socializing'] == 'Yes' else 0
    
    # Create DataFrame
    df_user = pd.DataFrame([user_data])
    
    # Make prediction
    prediction = model.predict(df_user)[0]
    probability = model.predict_proba(df_user)[0]
    
    return prediction, probability

def display_results(prediction, probability):
    """Display prediction results"""
    st.markdown("### 🎯 Your Personality Prediction")
    
    if prediction == 0:  # Extrovert
        personality = "Extrovert"
        emoji = "🦁"
        description = "You tend to be outgoing, social, and energized by interactions with others!"
    else:  # Introvert
        personality = "Introvert"
        emoji = "🦉"
        description = "You tend to be reflective, prefer solitude, and recharge through alone time!"
    
    # Display prediction card
    st.markdown(f"""
    <div class="prediction-card">
        <h2>{emoji} {personality} {emoji}</h2>
        <p style="font-size: 1.2rem;">{description}</p>
        <p style="font-size: 1rem; opacity: 0.9;">Confidence: {max(probability)*100:.1f}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show confidence percentages
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Extrovert Probability", f"{probability[0]*100:.1f}%")
    with col2:
        st.metric("Introvert Probability", f"{probability[1]*100:.1f}%")

def main():
    # Header
    st.markdown('<h1 class="main-header">🧠 Personality Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Discover if you\'re more of an Extrovert or Introvert</p>', unsafe_allow_html=True)
    
    # Load data and train model
    with st.spinner("Loading data and training model..."):
        df, imputer = load_and_prepare_data()
        
        if df is not None:
            model, accuracy = train_model(df)
            
            # Show model info
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Model Accuracy", f"{accuracy*100:.1f}%")
            with col2:
                st.metric("Algorithm", "Logistic Regression")
            with col3:
                st.metric("Training Data", "18,526 samples")
            
            st.markdown("---")
            
            # Create input form
            user_data = create_input_form()
            
            # Prediction button
            if st.button("🔮 Predict My Personality", type="primary", use_container_width=True):
                with st.spinner("Analyzing your characteristics..."):
                    prediction, probability = predict_personality(model, user_data)
                    display_results(prediction, probability)
                    
                    # Show insights
                    st.markdown("---")
                    st.markdown("### 💡 Insights")
                    
                    if prediction == 0:  # Extrovert
                        st.info("""
                        **Extrovert Characteristics:**
                        - You likely gain energy from social interactions
                        - You probably enjoy being around people
                        - You may prefer group activities over solo pursuits
                        - You tend to think out loud and process information through conversation
                        """)
                    else:  # Introvert
                        st.info("""
                        **Introvert Characteristics:**
                        - You likely recharge through alone time
                        - You probably prefer deep, meaningful conversations over small talk
                        - You may enjoy solitary activities and introspection
                        - You tend to think before speaking and process information internally
                        """)
                    
                    st.markdown("""
                    **Remember:** Personality is complex and exists on a spectrum. 
                    This prediction is based on behavioral patterns and should be taken as a general guide.
                    """)
        else:
            st.error("Could not load the training data. Please make sure the 'Data/train.csv' file exists.")

if __name__ == "__main__":
    main() 