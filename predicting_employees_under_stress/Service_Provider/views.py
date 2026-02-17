from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
import datetime
import xlwt
from django.http import HttpResponse
import numpy as np # linear algebra
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Create your views here.
from Remote_User.models import ClientRegister_Model,Predicting_Employee_Stress,detection_ratio,detection_accuracy
from .models import Admin_Model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check hardcoded admin first
        if admin == "Admin" and password =="Admin":
            request.session['admin_username'] = "Admin"
            return redirect('View_Remote_Users')
        
        # Try database admin if table exists
        try:
            admin_user = Admin_Model.objects.get(username=admin, password=password, is_active=True)
            request.session['admin_username'] = admin_user.username
            return redirect('View_Remote_Users')
        except:
            # Table doesn't exist or admin not found
            return render(request,'SProvider/serviceproviderlogin.html', {'error': 'Invalid credentials'})

    return render(request,'SProvider/serviceproviderlogin.html')

def View_Employee_Stress_Prediction_Type_Ratio(request):
    detection_ratio.objects.all().delete()
    ratio = ""
    kword = 'Low Stress'
    print(kword)
    obj = Predicting_Employee_Stress.objects.all().filter(Q(Prediction=kword))
    obj1 = Predicting_Employee_Stress.objects.all()
    count = obj.count();
    count1 = obj1.count();
    ratio = (count / count1) * 100
    if ratio != 0:
        detection_ratio.objects.create(names=kword, ratio=ratio)

    ratio1 = ""
    kword1 = 'More Stress'
    print(kword1)
    obj1 = Predicting_Employee_Stress.objects.all().filter(Q(Prediction=kword1))
    obj11 = Predicting_Employee_Stress.objects.all()
    count1 = obj1.count();
    count11 = obj11.count();
    ratio1 = (count1 / count11) * 100
    if ratio1 != 0:
        detection_ratio.objects.create(names=kword1, ratio=ratio1)

    obj = detection_ratio.objects.all()
    return render(request, 'SProvider/View_Employee_Stress_Prediction_Type_Ratio.html', {'objs': obj})

def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = Predicting_Employee_Stress.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def charts(request,chart_type):
    chart1 = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def charts1(request,chart_type):
    chart1 = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})

def View_Employee_Stress_Prediction_Type(request):
    obj =Predicting_Employee_Stress.objects.all()
    return render(request, 'SProvider/View_Employee_Stress_Prediction_Type.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'chart_type':like_chart})


def Download_Trained_DataSets(request):

    response = HttpResponse(content_type='application/ms-excel')
    # decide file name
    response['Content-Disposition'] = 'attachment; filename="PredictedData.xls"'
    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')
    # adding sheet
    ws = wb.add_sheet("sheet1")
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True
    # writer = csv.writer(response)
    obj = Predicting_Employee_Stress.objects.all()
    data = obj  # dummy method to fetch data.
    for my_row in data:
        row_num = row_num + 1

        ws.write(row_num, 0, my_row.employee_id, font_style)
        ws.write(row_num, 1, my_row.department, font_style)
        ws.write(row_num, 2, my_row.region, font_style)
        ws.write(row_num, 3, my_row.education, font_style)
        ws.write(row_num, 4, my_row.gender, font_style)
        ws.write(row_num, 5, my_row.recruitment_channel, font_style)
        ws.write(row_num, 6, my_row.Training_Time, font_style)
        ws.write(row_num, 7, my_row.age, font_style)
        ws.write(row_num, 8, my_row.Prformance_Rating, font_style)
        ws.write(row_num, 9, my_row.Years_at_company, font_style)
        ws.write(row_num, 10, my_row.Working_Hours, font_style)
        ws.write(row_num, 11, my_row.Flexible_Timings, font_style)
        ws.write(row_num, 12, my_row.Workload_level, font_style)
        ws.write(row_num, 13, my_row.Monthly_Income, font_style)
        ws.write(row_num, 14, my_row.Work_Satisfaction, font_style)
        ws.write(row_num, 15, my_row.Percent_salary_hike, font_style)
        ws.write(row_num, 16, my_row.companies_worked, font_style)
        ws.write(row_num, 17, my_row.Marital_Status, font_style)
        ws.write(row_num, 18, my_row.Prediction, font_style)



    wb.save(response)
    return response

def Train_Test_DataSets(request):
    detection_accuracy.objects.all().delete()

    df = pd.read_csv('Employee_Datasets.csv', encoding='latin-1')
    df
    df.columns

    def apply_results(results):
        if (results == 'No'):
            return 0
        elif (results == 'Yes'):
            return 1

    df['Results'] = df['Stress_status'].apply(apply_results)

    X = df['employee_id']
    y = df['Results']

    print("RID")
    print(X)
    print("Results")
    print(y)

    cv = CountVectorizer(lowercase=False, strip_accents='unicode', ngram_range=(1, 1))
    # X = cv.fit_transform(df['employee_id'].apply(lambda x: np.str_(X)))
    X = cv.fit_transform(X)

    models = []
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    X_train.shape, X_test.shape, y_train.shape

    print("Naive Bayes")

    from sklearn.naive_bayes import MultinomialNB
    NB = MultinomialNB()
    NB.fit(X_train, y_train)
    predict_nb = NB.predict(X_test)
    naivebayes = accuracy_score(y_test, predict_nb) * 100
    print(naivebayes)
    print(confusion_matrix(y_test, predict_nb))
    print(classification_report(y_test, predict_nb))
    models.append(('naive_bayes', NB))
    detection_accuracy.objects.create(names="Naive Bayes", ratio=naivebayes)

    # SVM Model
    print("SVM")
    from sklearn import svm
    lin_clf = svm.LinearSVC()
    lin_clf.fit(X_train, y_train)
    predict_svm = lin_clf.predict(X_test)
    svm_acc = accuracy_score(y_test, predict_svm) * 100
    print(svm_acc)
    print("CLASSIFICATION REPORT")
    print(classification_report(y_test, predict_svm))
    print("CONFUSION MATRIX")
    print(confusion_matrix(y_test, predict_svm))
    models.append(('svm', lin_clf))
    detection_accuracy.objects.create(names="SVM", ratio=svm_acc)


    print("Logistic Regression")

    from sklearn.linear_model import LogisticRegression
    reg = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    print("ACCURACY")
    print(accuracy_score(y_test, y_pred) * 100)
    print("CLASSIFICATION REPORT")
    print(classification_report(y_test, y_pred))
    print("CONFUSION MATRIX")
    print(confusion_matrix(y_test, y_pred))
    models.append(('logistic', reg))

    detection_accuracy.objects.create(names="Logistic Regression", ratio=accuracy_score(y_test, y_pred) * 100)


    print("KNeighborsClassifier")

    from sklearn.neighbors import KNeighborsClassifier
    kn = KNeighborsClassifier()
    kn.fit(X_train, y_train)
    knpredict = kn.predict(X_test)
    print("ACCURACY")
    print(accuracy_score(y_test, knpredict) * 100)
    print("CLASSIFICATION REPORT")
    print(classification_report(y_test, knpredict))
    print("CONFUSION MATRIX")
    print(confusion_matrix(y_test, knpredict))
    detection_accuracy.objects.create(names="KNeighborsClassifier", ratio=accuracy_score(y_test, knpredict) * 100)

    print("Decision Tree Classifier")
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    dtcpredict = dtc.predict(X_test)
    print("ACCURACY")
    print(accuracy_score(y_test, dtcpredict) * 100)
    print("CLASSIFICATION REPORT")
    print(classification_report(y_test, dtcpredict))
    print("CONFUSION MATRIX")
    print(confusion_matrix(y_test, dtcpredict))
    models.append(('DecisionTreeClassifier', dtc))
    detection_accuracy.objects.create(names="Decision Tree Classifier", ratio=accuracy_score(y_test, dtcpredict) * 100)

    print("SGD Classifier")
    from sklearn.linear_model import SGDClassifier
    sgd_clf = SGDClassifier(loss='hinge', penalty='l2', random_state=0)
    sgd_clf.fit(X_train, y_train)
    sgdpredict = sgd_clf.predict(X_test)
    print("ACCURACY")
    print(accuracy_score(y_test, sgdpredict) * 100)
    print("CLASSIFICATION REPORT")
    print(classification_report(y_test, sgdpredict))
    print("CONFUSION MATRIX")
    print(confusion_matrix(y_test, sgdpredict))
    models.append(('SGDClassifier', sgd_clf))
    detection_accuracy.objects.create(names="SGD Classifier", ratio=accuracy_score(y_test, sgdpredict) * 100)


    predicts = 'Results.csv'
    df.to_csv(predicts, index=False)
    df.to_markdown

    obj = detection_accuracy.objects.all()


    return render(request,'SProvider/Train_Test_DataSets.html', {'objs': obj})

def Add_Admin(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            
            if Admin_Model.objects.filter(username=username).exists():
                return render(request, 'SProvider/Add_Admin.html', {'error': 'Username already exists'})
            
            Admin_Model.objects.create(username=username, password=password, email=email)
            return render(request, 'SProvider/Add_Admin.html', {'success': 'Admin added successfully'})
    except:
        return render(request, 'SProvider/Add_Admin.html', {'error': 'Admin table not created yet. Run SQL script first.'})
    
    return render(request, 'SProvider/Add_Admin.html')

def View_Admins(request):
    try:
        admins = Admin_Model.objects.all().order_by('-created_date')
        return render(request, 'SProvider/View_Admins.html', {'admins': admins})
    except:
        return render(request, 'SProvider/View_Admins.html', {'error': 'Admin table not created yet. Run SQL script first.'})

def Delete_Admin(request, admin_id):
    try:
        admin = Admin_Model.objects.get(id=admin_id)
        admin.delete()
    except:
        pass
    return redirect('View_Admins')