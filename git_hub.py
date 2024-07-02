print("""git은 컴퓨터내에서 사용할 수 있는 버전관리시스템입니다. 프로그래밍을 하다보면 계속 업데이트를 해야하는데 이때 이전 버전과 수정 버전들을 편리하게 관리할 수 있도록 만들어주는 것이 git입니다.

git을 설치한 후 터미널에서 git config --global user.name [유저네임]과 git config --global user.email [이메일주소] github와 연결할 수 있습니다.

깃허브의 프로세스는 우선 컴퓨터 내의 작업공간에서 작업을 하고 commit을 하기 전 파일들을 모아두는 곳인 Staging Area에 add한 후 커밋들의 저장소에 commit하여 push를 통해 최종적으로 깃허브의 repository 에 올리게 됩니다.
(git add -> git commit -> git push)

Github와 컴퓨터의 저장공간을 연결하면 이후 프로그램을 수정했을때 간단한 명령어 입력으로 손쉽게 업데이트된 내역을 github에 올릴 수 있게됩니다.

연동하는 방법은 github에서 repository(repo)를 만들고 링크를 가져온 다음 컴퓨터 안의 작업중인 폴더에서 open Git Bash here을 클릭합니다

이후 Bash에 echo “내용” >> README.md 를 입력하여 README.md 파일에 내용, 즉 프로젝트에 대한 설명을 기입합니다
git init 으로 저장소를 초기화합니다
git add [파일명]으로 파일을 추가합니다
git commit -m “[커밋메시지]” 로 변경사항을 커밋하고 -m 옵션으로 수정사항을 [커밋메시지] 부분에 남깁니다

git branch -M main 으로 브랜치를 만듭니다. 브랜치의 이름은 주로 main 또는 master를 사용합니다. 여기서 브랜치란 프로젝트가 존재하는 저장 공간인 repository 안에서 독립적으로 작업을 하기 위한 공간이라고 합니다. (자세한 내용은 깃허브를 더 사용하면서 알아가야할 것 같습니다)

git remote add origin [git url] 로 origin이라는 별칭의 원격 저장소(깃허브)를 추가합니다

push -u origin main 으로 위에서 만든 main 브랜치를 origin(원격저장소)에 푸쉬합니다.


""")