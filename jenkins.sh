@ECHO OFF

sonar-scanner-3.3.0.1492-linux/bin/sonar-scanner -Dsonar.projectKey=Versusfinder -Dsonar.organization=skogarmadr-github -Dsonar.sources=. -Dsonar.host.url=https://sonarcloud.io \
-Dsonar.login=c21936d712b162805304fa999c443ef933b4b24

PAUSE
