# 🏥 Chronic Disease Prediction System

A comprehensive AI-powered web application for predicting chronic kidney disease using machine learning. This system provides a user-friendly interface for medical professionals and patients to input test results and receive predictions through a multi-step analysis process.

## 🌟 Features

- **Multi-Step Analysis Process**: Organized workflow through Blood Test → Urine Test → Medical History
- **AI-Powered Predictions**: Uses trained machine learning model for accurate disease prediction
- **Professional Medical Interface**: Clean, hospital-grade UI design with intuitive navigation
- **Session Management**: Secure data handling across multiple form steps
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Validation**: Input validation and error handling at each step
- **Comprehensive Results**: Detailed prediction results with data summary

## 🛠️ Technology Stack

- **Backend**: Python Flask Framework
- **Machine Learning**: Scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Processing**: NumPy, Pandas
- **Model**: Trained ML model (chronic_model.pkl)
- **Deployment**: Local development server



## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone https://github.com/Surya-0609/Chronic-Disease-Prediction.git
cd Chronic-Disease-Prediction
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python app.py
```

### 6. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 💻 Usage

### Step-by-Step Process

1. **Home Page**: Overview of the 3-step analysis process
2. **Blood Test Results**: Enter blood test parameters
   - Packed Cell Volume (PCV)
   - Haemoglobin (g/dL)
   - Serum Creatinine (mg/dL)
   - Blood Urea (mg/dL)
   - Blood Glucose Random (mg/dL)

3. **Urine Test Results**: Enter urine analysis data
   - Specific Gravity
   - Albumin (mg/dL)
   - Red Blood Cell Count

4. **Medical History**: Complete medical background
   - Hypertension (Yes/No)
   - Diabetes Mellitus (Yes/No)

5. **Results**: View AI prediction and data summary

### Sample Input Values
For testing purposes, you can use these sample values:
```
Blood Test:
- PCV: 44.0
- Haemoglobin: 12.5
- Serum Creatinine: 1.2
- Blood Urea: 25.0
- Blood Glucose: 120.0

Urine Test:
- Specific Gravity: 1.025
- Albumin: 0.5
- RBC Count: 2.0

Medical History:
- Hypertension: No (0)
- Diabetes: No (0)
```

## 🧠 Machine Learning Model

The application uses a trained machine learning model that analyzes:
- **10 input features** from medical tests
- **Binary classification** (Disease/No Disease)
- **High accuracy** prediction system
- **Robust preprocessing** and validation

### Model Features
- Trained on comprehensive kidney disease dataset
- Handles missing values and outliers
- Optimized for medical diagnosis accuracy
- Regular model validation and updates

## 🎨 User Interface

### Design Principles
- **Medical-Grade Interface**: Professional healthcare application design
- **Progressive Disclosure**: Information revealed step-by-step
- **Visual Feedback**: Clear progress indicators and status messages
- **Accessibility**: WCAG compliant design elements
- **Responsive Layout**: Mobile-first design approach

### Color Scheme
- **Home Page**: Purple gradient background
- **Form Pages**: Light blue gradient background
- **Success**: Green indicators
- **Warning**: Red indicators
- **Neutral**: Gray for disabled elements

## 🔒 Security Features

- **Session Management**: Secure data storage between steps
- **Input Validation**: Server-side and client-side validation
- **Error Handling**: Comprehensive error management
- **Data Privacy**: Local processing, no external data transmission

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/blood-test` | GET | Blood test form |
| `/submit-blood-test` | POST | Save blood test data |
| `/urine-test` | GET | Urine test form |
| `/submit-urine-test` | POST | Save urine test data |
| `/medical-history` | GET | Medical history form |
| `/predict` | POST | Generate prediction |

## 🧪 Testing

### Manual Testing
1. Navigate through all form steps
2. Test with various input combinations
3. Verify error handling
4. Check responsive design on different devices

### Sample Test Cases
- Valid medical data → Successful prediction
- Invalid input values → Error messages
- Incomplete forms → Validation errors
- Navigation between steps → Data persistence

## 🚀 Deployment

### Local Development
The application is currently configured for local development with Flask's built-in server.

### Production Deployment
For production deployment, consider:
- **WSGI Server**: Gunicorn, uWSGI
- **Reverse Proxy**: Nginx, Apache
- **Environment Variables**: Secret keys, database URLs
- **SSL Certificate**: HTTPS encryption
- **Database**: PostgreSQL, MySQL for production data

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 Python style guide
- Add comments for complex logic
- Test all new features thoroughly
- Update documentation as needed

## 🐛 Troubleshooting

### Common Issues

**Issue**: Model file not found
```bash
Error: FileNotFoundError: chronic_model.pkl not found
Solution: Ensure chronic_model.pkl is in the project root directory
```

**Issue**: Import errors
```bash
Error: ModuleNotFoundError: No module named 'flask'
Solution: Activate virtual environment and install requirements
```

**Issue**: Port already in use
```bash
Error: Address already in use
Solution: Change port in app.py or kill process using port 5000
```

## 📈 Future Enhancements

- [ ] **Database Integration**: PostgreSQL/MySQL for data storage
- [ ] **User Authentication**: Login/registration system
- [ ] **History Tracking**: Save and view past predictions
- [ ] **Advanced Analytics**: Statistical analysis and trends
- [ ] **Multi-language Support**: Internationalization
- [ ] **PDF Reports**: Downloadable prediction reports
- [ ] **Mobile App**: Native mobile application
- [ ] **API Documentation**: Swagger/OpenAPI integration


## 🙏 Acknowledgments

- Medical professionals who provided domain expertise
- Open source machine learning community
- Flask and Scikit-learn development teams
- Healthcare data providers for training datasets



## ⚠️ Medical Disclaimer

**Important**: This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

---

**Made with ❤️ for better healthcare through AI**
