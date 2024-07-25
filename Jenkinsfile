pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                git 'https://github.com/tu_usuario/tu_repositorio.git'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas Unitarias') {
            steps {
                sh 'pytest'
            }
        }
        stage('Desplegar Aplicación') {
            steps {
                // Aquí puedes agregar los pasos para desplegar tu aplicación
                echo 'Desplegando la aplicación en el entorno de prueba'
                // Ejemplo: sh 'deploy.sh'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completado con éxito'
        }
        failure {
            echo 'Pipeline fallido'
        }
    }
}
