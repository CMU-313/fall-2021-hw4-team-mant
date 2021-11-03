# Software Engineering for Machine Learning Assignment
### API Description
Our API has one main endpoint /predict. 

How it should be called: To predict if a student will be a quality student, you can perform a GET request to the `localhost:5000/predict` endpoint with the following fields (data it expects):
* address : student’s home address type (binary: “U” - urban or “R” - rural)
* Pstatus : parent’s cohabitation status (binary: “T” - living together or “A” - apart)
* Medu : mother’s education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
* Fedu : father’s education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
* studytime : weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
* activities : extra-curricular activities (binary: yes or no)
* higher : wants to take higher education (binary: yes or no)
* internet : Internet access at home (binary: yes or no)
* absences : number of school absences (numeric: from 0 to 93)
* failures : number of past class failures (numeric: n if 1<=n<3, else 4)


This results in the example path `localhost:5000/predict?address=U&Pstatus=T&Medu=4&Fedu=4&studytime=4&activities=yes&higher=yes&internet=yes&absences=0&failures=0`

Preconditions for the service:
Other than the variables/data described above, there are no preconditions for the service.

The API will output 1 or 0 with a 1 corresponding to a 'quality student' (a student with G3 >= 15) and 0 corresponding to a student with G3 < 15.

### Features Used in Training
The features we used in our training were student's home address type, parent cohabitation status, numeric ranking of mother's education, numeric ranking father's education, weekly studytime in hours, whether or not the student participates in activites, the desire to go into higher education, whether or not the student has internet access at home, the number of school absences and the number of past class failures. A student's home environment plays a large role in their attitude towards school, which is why we prioritized the first four features listed above, as well as the internet access feature. The amount of time a student spends studying and whether or not they dedicate time to extracurricular activities will also impact how much time they get to work on their assignments and study for exams, which impacts overall grades. Finally, we believed that higher absence and failure rates are strongly inversely correlated with high performance, so we added these two features as well.

The baseline performance we found had a test accuracy of 52%. The performance of our model after we added these features had a test accuracy of around 85%, which means that the addition of the features above caused an improvement of about 30% testing accuracy in the model. 

### Deployment Instructions
The API can be deployed by following the following steps:
* Clone this repository
* `cd dockerfile`
* `docker build -t ml:latest .`
* `docker run -d -p 5000:5000 ml`
  * If the docker container instantly exits, uncomment the `RUN pip install scikit-learn==0.24.1` line in the Dockerfile. This change is necessary if the model was built using an older version of sklearn.


### Testing
