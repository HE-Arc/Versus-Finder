pipeline {
  agent {
    docker { image 'python:3.7.1' }
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python --version'
      }
    }
    stage('QualityTest') { 
            steps {
			sh '(mvn clean test)'
		    sh '(mvn sonar:sonar -Dsonar.projectKey=Versusfinder -Dsonar.organization=skogarmadr-github -Dsonar.host.url=https://sonarcloud.io -Dsonar.login=3d0cf503c64084102358a4c51068f89e69107699)'
	    }
    }
  }

}