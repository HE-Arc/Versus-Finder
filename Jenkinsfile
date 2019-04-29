pipeline {
  agent {
    docker { image 'python:3.7.1' }
  }
  environment {
    PATH = "./sonar-scanner-3.3.0.1492-linux/bin:$PATH"
  }

  stages {
        stage ('build') {
      steps {
        echo "PATH is: $PATH"
      }
    }

    stage('Install dependencies') {
      steps {
        sh 'sonar-scanner -h'
      }
    }
    stage('Test') {
      steps {
        sh 'python --version'
      }
    }
  
    stage('QualityTest') { 
            steps {
		    sh '(sonar-scanner  -Dsonar.projectKey=Versusfinder   -Dsonar.organization=skogarmadr-github   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io -Dsonar.login=c21936d712b162805304fa999c443ef933b4b246)'
	    }
    }
  }
}