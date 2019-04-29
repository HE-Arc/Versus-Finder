pipeline {
  agent {
    docker { image 'python:3.7.1' }
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'echo test'
      }
    }
    stage('Test') {
      steps {
        sh 'python --version'
      }
    }
    stage('Sonarqube analysis') {
        steps {
        script {
                scannerHome = tool 'SonarScanner';
            }
        withSonarQubeEnv('SonarQube') {
            sh "${scannerHome}/bin/sonar-scanner -h" 
        }

        }
        }
    stage('QualityTest') { 
            steps {
        sh 'echo "PATH is: $PATH"'
		    sh '(./sonar-scanner  -Dsonar.projectKey=Versusfinder   -Dsonar.organization=skogarmadr-github   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io )'
	    }
    }
  }
}