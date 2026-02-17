# Employee Stress Prediction System

A machine learning-based web application that predicts employee stress levels using multiple algorithms to help organizations proactively manage employee wellness and prevent burnout.

## 🆕 New Features & Updates

### 🎨 Modern UI Design
- **Bootstrap 5 Integration**: Complete UI overhaul with modern responsive design
- **Professional Styling**: Gradient backgrounds, card layouts, and smooth animations
- **Mobile Responsive**: Optimized for all device sizes
- **Color-coded Results**: Visual indicators for stress levels (green/red)

### 🔐 Enhanced Admin Management
- **Multiple Administrators**: Support for unlimited admin accounts
- **Database-driven**: Admin credentials stored securely in database
- **Admin CRUD Operations**: Add, view, and delete administrators
- **Session Management**: Proper login session handling
- **Backward Compatibility**: Original Admin/Admin login still works

### 📊 Improved Analytics
- **Visual Charts**: Enhanced prediction ratio displays with progress bars
- **Performance Metrics**: Color-coded accuracy indicators for ML algorithms
- **Data Visualization**: Modern card-based layouts for better readability
- **Export Functionality**: Download prediction data as Excel files

## 🎯 Project Overview

This Django-based system analyzes 18+ employee parameters to predict stress levels ("Low Stress" or "More Stress") using ensemble machine learning techniques. It provides both employee and admin interfaces for comprehensive stress management.

## 🚀 Quick Start Guide

### For New Admins:
1. **Login**: Use Admin/Admin or SuperAdmin/SuperAdmin123
2. **Add Admins**: Navigate to "Manage Admins" → "Add New Admin"
3. **View Analytics**: Check prediction ratios and ML accuracy
4. **Export Data**: Download prediction results as Excel

### For Employees:
1. **Register**: Create account at http://127.0.0.1:8000/
2. **Login**: Use your credentials
3. **Predict Stress**: Fill out the 18-parameter form
4. **View Results**: Get color-coded stress level prediction

## 🔧 Technology Stack

- **Backend**: Django 4.x (Python Web Framework)
- **Database**: MySQL 8.0+
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **UI Framework**: Modern responsive design with Bootstrap 5
- **Export**: Excel (xlwt)

## 🤖 Machine Learning Algorithms

The system uses **6 different algorithms** with ensemble voting:

1. **Naive Bayes (MultinomialNB)** - Probability-based classification
2. **Support Vector Machine (LinearSVC)** - Optimal decision boundary
3. **Logistic Regression** - Binary classification with interpretability
4. **K-Nearest Neighbors** - Instance-based learning
5. **Decision Tree Classifier** - Rule-based decisions
6. **SGD Classifier** - Efficient linear classification

**Final Prediction**: Voting Classifier (combines all 6 algorithms)

## 📋 Prerequisites

### Software Requirements
- **Python**: 3.8+ (Recommended: 3.9 or 3.10)
- **MySQL Server**: 8.0+ or MySQL Workbench
- **Git**: For version control (optional)

### System Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB free space

## 🚀 Installation Guide

### Step 1: Clone/Download Project
```bash
# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download ZIP and extract
# Extract to: D:\downloads\Innovative\Predicting_Employees_Under_Stress\
```

### Step 2: Set Up Python Environment
```bash
# Create virtual environment
python -m venv wesad_env

# Activate environment
# Windows:
wesad_env\Scripts\activate
# macOS/Linux:
source wesad_env/bin/activate
```

### Step 3: Install Python Dependencies
```bash
pip install django==4.2.7
pip install mysqlclient
pip install pandas==2.1.3
pip install numpy==1.24.3
pip install scikit-learn==1.3.2
pip install xlwt==1.3.0
```

**Alternative**: Create `requirements.txt` and install:
```bash
pip install -r requirements.txt
```

### Step 4: MySQL Database Setup

#### 4.1 Install MySQL
- Download MySQL Server 8.0+ from [mysql.com](https://dev.mysql.com/downloads/)
- Install MySQL Workbench (GUI tool)
- Set root password during installation

#### 4.2 Create Database
Open MySQL Workbench and run:
```sql
CREATE DATABASE predicting_employees_under_stress;
```

#### 4.3 Import Database Schema
**Method 1: Using MySQL Workbench**
1. Go to **Server** → **Data Import**
2. Select **Import from Self-Contained File**
3. Browse to: `Database/predicting_employees_under_stress.sql`
4. Target Schema: `predicting_employees_under_stress`
5. Click **Start Import**

**Method 2: Command Line**
```bash
mysql -u root -p predicting_employees_under_stress < Database/predicting_employees_under_stress.sql
```

#### 4.4 Add Admin Management Table (Optional)
For multiple admin support, run the admin table script:
```bash
mysql -u root -p predicting_employees_under_stress < add_admin_table.sql
```

### Step 5: Configure Django Settings

Edit `predicting_employees_under_stress/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'predicting_employees_under_stress',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',  # Update this
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### Step 6: Run Django Application

Navigate to project directory:
```bash
cd "Predicting_Employees_Under_Stress/predicting_employees_under_stress"
```

Run migrations and start server:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 🌐 Accessing the Application

### URLs
- **Main Application**: http://127.0.0.1:8000/
- **Employee Login**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/serviceproviderlogin/

### Default Credentials
- **Admin Username**: Admin
- **Admin Password**: Admin
- **Additional Admin**: SuperAdmin/SuperAdmin123 (if admin table created)

## 📊 Features

### For Employees
- **Registration & Login**: Secure user authentication
- **Stress Prediction**: Input personal/work details for prediction
- **Profile Management**: View and update profile information

### For Administrators
- **User Management**: View all registered employees
- **Admin Management**: Add, view, and delete multiple administrators
- **Model Training**: Train ML algorithms with new data
- **Analytics Dashboard**: View prediction accuracy and statistics
- **Data Export**: Download prediction results as Excel files
- **Visualization**: Charts showing stress prediction ratios
- **Modern UI**: Professional Bootstrap 5 interface

## 📈 Input Parameters

The system analyzes these employee factors:

### Personal Information
- Employee ID, Age, Gender, Education Level, Marital Status

### Work Environment
- Department, Region, Working Hours, Flexible Timings, Workload Level

### Performance & Experience
- Performance Rating, Years at Company, Training Time, Companies Worked

### Compensation & Satisfaction
- Monthly Income, Salary Hike Percentage, Work Satisfaction, Recruitment Channel

## 🔍 How It Works

1. **Data Input**: Employee enters personal and work-related information
2. **Preprocessing**: System processes and vectorizes the input data
3. **Model Prediction**: 6 ML algorithms analyze the data independently
4. **Ensemble Decision**: Voting classifier combines all predictions
5. **Result**: System outputs "Low Stress" or "More Stress" prediction
6. **Storage**: Results saved to database for future analysis

## 📁 Project Structure

```
Predicting_Employees_Under_Stress/
├── Database/
│   └── predicting_employees_under_stress.sql    # Database schema
├── add_admin_table.sql                          # Admin management table
├── predicting_employees_under_stress/           # Django project
│   ├── manage.py                                # Django management
│   ├── predicting_employees_under_stress/       # Settings & URLs
│   ├── Remote_User/                             # Employee app
│   │   ├── models.py                            # Database models
│   │   ├── views.py                             # Business logic
│   │   └── migrations/                          # Database migrations
│   ├── Service_Provider/                        # Admin app
│   │   ├── views.py                             # Admin functions
│   │   └── models.py                            # Admin models
│   ├── Template/                                # HTML templates
│   │   ├── htmls/                               # Modern Bootstrap 5 templates
│   │   └── images/                              # Static images
│   ├── Employee_Datasets.csv                    # Training data
│   └── Results.csv                              # Prediction results
└── README.md                                    # This file
```

## 🛠️ Troubleshooting

### Common Issues

**1. MySQL Connection Error**
```
Error: (1049, "Unknown database 'predicting_employees_under_stress'")
```
**Solution**: Create database in MySQL Workbench first

**2. Module Not Found Error**
```
ModuleNotFoundError: No module named 'xlwt'
```
**Solution**: Install missing packages: `pip install xlwt`

**3. Django URL Import Error**
```
ImportError: cannot import name 'url' from 'django.conf.urls'
```
**Solution**: Already fixed in current version (uses `path` and `re_path`)

**4. Permission Denied (MySQL)**
**Solution**: Check MySQL credentials in `settings.py`

### Performance Tips
- Use Python 3.9+ for better performance
- Ensure MySQL server has sufficient memory
- Close unnecessary applications during model training

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For issues and questions:
- Create an issue in the repository
- Check troubleshooting section above
- Verify all prerequisites are installed correctly

## 🎯 Future Enhancements

- Real-time stress monitoring dashboard
- Integration with HR management systems
- Mobile application support
- Advanced visualization with D3.js
- API endpoints for third-party integration
- Multi-language support

---

**Note**: This system is designed for research and educational purposes. For production use in actual HR environments, additional security measures and compliance considerations should be implemented.