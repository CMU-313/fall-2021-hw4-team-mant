# Software Engineering for Machine Learning Assignment
### API Description
Our API has one main endpoint /predict. To predict if a student will be a quality student, you can perform a GET request to the `localhost:5000/predict` endpoint with the following fields:
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

### Features Used in Training

### Deployment Instructions
The API can be deployed by following the following steps:
* Clone this repository
* `cd dockerfile`
* `docker build -t ml:latest .`
* `docker run -d -p 5000:5000 ml`
  * If the docker container instantly exits, uncomment the `RUN pip install scikit-learn==0.24.1` line in the Dockerfile. This change is necessary if the model was built using an older version of sklearn.


### Testing
