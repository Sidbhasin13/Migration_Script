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
      dir('sources')
      steps{
          sh 'python script.py'
      }
    }
  }
}
