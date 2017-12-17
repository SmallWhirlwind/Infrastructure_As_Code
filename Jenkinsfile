def SSHCredentialsId= '94afa32c-7074-44fc-a363-2fbbe377eca1'
node {
    withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: "${SSHCredentialsId}",usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
        stage('Buile') {
            sh '''
            sudo ansible-playbook -i hosts Infrastructure.yml --user $USERNAME --extra-vars ansible_ssh_pass=$PASSWORD
            '''
        }
    }
}