from flask import Flask, request, render_template, redirect, Blueprint
import models as mo

bp = Blueprint('rank', __name__, url_prefix='/rank')

service = mo.tmapService()

@bp.route('/regionRank', methods=['POST'])
def regionRank():
    y = request.form['y']
    rank:list = service.regionRank(y=y)
    return render_template('rank/regionRank.html', rank=rank, y=y)

'''
@bp.route('/route-info', methods=['POST'])
def route_info():
    routeid = request.form['routeid']
    bus:mo.Bus = service.getRouteInfo(routeId=routeid)
    return render_template('bus/businfo.html', bus=bus)


@bp.route('/regionRank', methods=['POST'])
def regionRank():
    areaNm = request.form['areaNm']
    rank = service.regionRank(areaNm=areaNm)
    return render_template('rank/regionRank.html', rank=rank)
'''