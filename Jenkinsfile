pipeline {

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub.id')
        BUILD_NUMBER = "${env.BUILD_ID}"
        GITHUB_USERNAME = "lirond101"
        GITHUB_EMAIL = "lirond101@gmail.com"
        TARGET_BRANCH = "master"
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
        stage('Info Docker') {
            steps {
                container('dind') {
                    sh 'docker info'
                }
            }
        }
    }
}
