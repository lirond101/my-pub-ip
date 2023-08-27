pipeline {

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub.id')
        TAG = VersionNumber (versionNumberString: '${BUILD_DATE_FORMATTED, "ddMMyyyy"}-jenkins-cicd-${BUILDS_TODAY}')
        GITHUB_USERNAME = "lirond101"
        GITHUB_EMAIL = "lirond101@gmail.com"
    }
    agent {
        kubernetes {
            yaml '''
                apiVersion: v1
                kind: Pod
                metadata:
                  namespace: jenkins
                  labels:
                    app: dind
                  name: dind
                spec:
                  containers:
                  - name: dind
                    image: docker:19.03.11-dind
                    securityContext:
                      privileged: true
                    tty: true
                    volumeMounts:
                      - name: docker-graph-storage
                        mountPath: /var/lib/docker
                  volumes:
                    - name: docker-graph-storage
                      emptyDir: {}
                '''
        }
    }
    stages {
      stage('Clone') {
          steps {
              git branch: 'main', credentialsId: 'github', url: 'git@github.com:lirond101/my-pub-ip.git'
          }
      }

      stage('Build') {
          steps {
              container('dind') {
                  sh 'docker build --network=host -t lirondadon/my-pub-ip:$TAG .'
              }
          }
      }

      stage('Test') {
          steps {
              container('dind') {
                  sh 'docker run -d --name my-pub-ip lirondadon/my-pub-ip:$TAG'
                  sh 'docker exec my-pub-ip pytest'
              }
          }
      }

      stage('Push') {
          steps {
              container('dind') {
                  sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                  sh 'docker push lirondadon/my-pub-ip:$TAG'
              }
          }
      }

      stage('Deploy') {
          steps {
              build job: "CD-my-pub-ip", wait: true, parameters: [string(name: 'TAG', value:TAG)]
          }
      }
   }
}
