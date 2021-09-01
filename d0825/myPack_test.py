import myPack.service as service
# 서비스 파일 전체를 임포트하는거
service.addArticle()
service.delArticle()
service.getArticle()
service.editArticle()

##########################################

from myPack.service import addArticle
#서비스파일에서 애드아티클만 임포트하는 것.
addArticle()