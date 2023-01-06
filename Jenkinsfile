pipeline {
  agent any
  environment {
    BRANCH = "${BRANCH_NAME}"
  }
  stages {
    stage('Build') {
      agent {
              docker {
                  image 'python:3.11.1-alpine3.17' 
              }
            }
      when {
          branch 'main'
      }
      steps{
          sh 'python script.py'
      }
    }
  }
}
