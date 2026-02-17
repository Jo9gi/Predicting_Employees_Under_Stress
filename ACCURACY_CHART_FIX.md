# Accuracy Chart Fix - Summary

## 🐛 Problem Found

Both accuracy chart sections were showing the **same graph** because they were using the same data source.

### Before (Incorrect):
```python
def charts1(request, chart_type):
    chart1 = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request, "SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})

def likeschart(request, like_chart):
    charts = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))  # ❌ SAME DATA
    return render(request, "SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})
```

## ✅ Solution Applied

Changed `likeschart` to use **different data source**:

### After (Correct):
```python
def charts1(request, chart_type):
    chart1 = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request, "SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})

def likeschart(request, like_chart):
    charts = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))  # ✅ DIFFERENT DATA
    return render(request, "SProvider/likeschart.html", {'form':charts, 'chart_type':like_chart})
```

## 📊 Data Sources Explained

| Chart Function | Data Source | Shows |
|---------------|-------------|-------|
| **charts** | `detection_ratio` | Stress prediction ratios (Low Stress vs More Stress) |
| **charts1** | `detection_accuracy` | ML algorithm accuracy (Naive Bayes, SVM, etc.) |
| **likeschart** | `detection_ratio` | Stress prediction ratios (different view) |
| **dislikeschart** | (needs checking) | - |

## 🔧 Files Modified

1. **Service_Provider/views.py** - Fixed `likeschart` function
2. **Template/htmls/SProvider/likeschart.html** - Updated variable name consistency

## 🧪 How to Test

1. Run: `python manage.py runserver`
2. Login as admin
3. Navigate to accuracy charts section
4. Verify:
   - **charts1** shows ML algorithm accuracy
   - **likeschart** shows stress prediction ratios
   - Both charts now display **different data**

## 📝 Expected Results

- **Chart 1 (charts1)**: Shows accuracy of 6 ML algorithms (Decision Tree, KNN, Logistic Regression, Naive Bayes, SGD, SVM)
- **Chart 2 (likeschart)**: Shows stress prediction distribution (Low Stress % vs More Stress %)
