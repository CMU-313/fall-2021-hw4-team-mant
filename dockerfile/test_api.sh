#!/bin/bash
test1=$(curl http://localhost:5000/predict\?Fedu=1\&Medu=3\&Pstatus=T\&absences=1\&activities=no\&address=U\&failures=0\&higher=yes\&internet=yes\&studytime=3)
test2=$(curl http://localhost:5000/predict\?Fedu=2\&Medu=3\&Pstatus=T\&absences=2\&activities=no\&address=U\&failures=0\&higher=yes\&internet=yes\&studytime=2)
test3=$(curl http://localhost:5000/predict\?Fedu=2\&Medu=3\&Pstatus=T\&absences=26\&activities=no\&address=U\&failures=0\&higher=yes\&internet=yes\&studytime=2)
test4=$(curl http://localhost:5000/predict)

# echo "${BASH_VERSION}"
if (($test1 != 1)) 
then
  echo "1 failed, returned 0, should be 1"
  exit 1
fi

if (($test2 != 0)) 
then
  echo "2 failed, return 0, should be 1"
  exit 2
fi

if (($test3 != 0)) 
then
  echo "3 failed, returned 1, should be 0"
  exit 3
fi

if (($test4 != 0 || $test4 != 1))
then
  echo "4 failed, returned 0 or 1, should not be 0 or 1"
  exit 4
fi

echo "Finished Testing!"
exit 0