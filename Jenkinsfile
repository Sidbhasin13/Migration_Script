pipeline {
  agent any
  
  environment {
    BRANCH = "${BRANCH_NAME}"
  }
  stages {
    stage('Build') {
//       when {
//           branch 'main'
//       }
      steps{
         sh 'python3 --version'
         sh 'pip install -r reqirements.txt'
         sh 'python3 script.py'
      }
    }
  }
}
