pipeline {
  agent any
  environment {
    BRANCH = "${BRANCH_NAME}"
  }
  stages {
    stage('Build') {
      when {
          branch 'main'
      }
      steps{
          sh 'python script.py'
      }
    }
  }
}
