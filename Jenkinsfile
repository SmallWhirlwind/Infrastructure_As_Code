def SSHCredentialsId= '94afa32c-7074-44fc-a363-2fbbe377eca1'
node {
    withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: "${SSHCredentialsId}",usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
        stage('Buile') {
        	git "https://github.com/SmallWhirlwind/Infrastructure_As_Code.git"
            sh '''
            sudo ansible-playbook -i hosts Infrastructure.yml --user $USERNAME --extra-vars ansible_ssh_pass=$PASSWORD
            '''
        }
        stage('Test') {
            sh '''
            sudo py.test -n 1 -v --host="192.168.33.101" --connection=ssh test_myinfra.py
            '''
        }
    }
}