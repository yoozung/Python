from flask import Flask, request, render_template, redirect, Blueprint
import models as mo
import pyautogui as pg

bp = Blueprint('rank', __name__, url_prefix='/rank')

RegionService = mo.RegionService()
nationWideService = mo.NationWideService()

@bp.route('/regionRank', methods=['POST', 'GET'])
def regionRank():
    page = request.args.get('page', type=int, default=1)  # 페이지
    y = request.form['y']
    rankData =  RegionService.getRegion(y)
    print(y)
    print(rankData)
    rank = rankData.paginate(page, per_page=5)
    print(rank)

    return render_template('rank/regionRank.html', rank=rank, page=page, y=y)

