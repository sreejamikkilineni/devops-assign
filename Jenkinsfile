pipeline { 
    agent any 

    stages { 
        stage('Build Docker Image') { 
            steps { 
                echo "Building Docker Image..."
                bat "docker build -t tictactoe:latest ."
            } 
        }
        stage('Docker login') {
            steps {
                bat 'docker login -u sreeja20082004 -p Sreeja@12'
            }
        }

        stage('push Docker image to docker hub'){
            steps{
                echo "push Docker image to docker hub"
                bat "docker tag tictactoe:latest sreeja20082004/sample:v1"

                bat "docker push sreeja20082004/sample:v1"
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                set KUBECONFIG = C:\\Users\\vr_ma\\.kube\\config
                kubectl cluster-info 
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }
    }

    post { 
        success { 
            echo 'Pipeline completed successfully! App deployed to Kubernetes.'
        } 
        failure { 
            echo 'Pipeline failed. Please check the logs for details.' 
        } 
    } 

}
