# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, Index, Integer, Numeric, SmallInteger, String, Table, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ActiveAnchorFuelTbl(db.Model):
    __tablename__ = 'active_anchor_fuel_tbl'

    id = db.Column(db.Integer, primary_key=True)
    anchor_uin = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    fans_uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    fans_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    fuel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveAuctionInfoTbl(db.Model):
    __tablename__ = 'active_auction_info_tbl'

    auction_id = db.Column(db.Integer, primary_key=True)
    winner_uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    winner_address_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    address_config = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    auction_title = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    start_price = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_price = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    join_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    start_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    stop_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveAuctionTbl(db.Model):
    __tablename__ = 'active_auction_tbl'
    __table_args__ = (
        db.Index('idx_user_action', 'uin', 'auction_id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    auction_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    price = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveIdeaTbl(db.Model):
    __tablename__ = 'active_idea_tbl'

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False)
    check_kind = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.Text, nullable=False)
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveImageTbl(db.Model):
    __tablename__ = 'active_image_tbl'

    image_id = db.Column(db.BigInteger, primary_key=True)
    auction_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    active_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    report_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    image_o = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_width = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    image_height = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    hash_key = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveSumAnchorSendTbl(db.Model):
    __tablename__ = 'active_sum_anchor_send_tbl'

    activeid = db.Column(db.Integer, primary_key=True, nullable=False)
    anchor_uin = db.Column(db.Integer, primary_key=True, nullable=False)
    send_uin = db.Column(db.Integer, primary_key=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    lastupdate = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveSumAnchorTbl(db.Model):
    __tablename__ = 'active_sum_anchor_tbl'
    __table_args__ = (
        db.Index('activeid', 'activeid', 'uin'),
    )

    id = db.Column(db.Integer, primary_key=True)
    activeid = db.Column(db.Integer, nullable=False)
    uin = db.Column(db.Integer, nullable=False)
    score = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    score1 = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    lastupdate = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveSumSendTbl(db.Model):
    __tablename__ = 'active_sum_send_tbl'
    __table_args__ = (
        db.Index('activeid', 'activeid', 'uin'),
    )

    id = db.Column(db.Integer, primary_key=True)
    activeid = db.Column(db.Integer, nullable=False)
    uin = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lastupdate = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveTbl(db.Model):
    __tablename__ = 'active_tbl'

    activeid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    outside_icon = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    outside_icon_start = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    outside_icon_end = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    inside_icon = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    inside_icon_start = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    inside_icon_end = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    active_start = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    active_end = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    banner_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    rank_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    admin = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    statistics_time = db.Column(db.Text)
    gift_json = db.Column(db.Text)
    active_kind = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, index=True, server_default=db.FetchedValue())
    style_kind = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    top_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    receive_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    statistics_kind = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class ActiveTicketTbl(db.Model):
    __tablename__ = 'active_ticket_tbl'

    activeid = db.Column(db.Integer, primary_key=True, nullable=False)
    uin = db.Column(db.Integer, primary_key=True, nullable=False)
    ticket = db.Column(db.Integer, nullable=False)


class ActiveUserAddressTbl(db.Model):
    __tablename__ = 'active_user_address_tbl'

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    user_name = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    phone = db.Column(db.String(15), nullable=False, server_default=db.FetchedValue())
    wechat = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    qq = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    address = db.Column(db.String(150), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ActiveUserTbl(db.Model):
    __tablename__ = 'active_user_tbl'
    __table_args__ = (
        db.Index('uin', 'activeid', 'uin'),
    )

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    activeid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    outside_icon = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    outside_icon_start = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    outside_icon_end = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    inside_icon = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    inside_icon_start = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    inside_icon_end = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    admin = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    check_status = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    reason = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    active_kind = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    memo = db.Column(db.Text)


class AnchorDataDay(db.Model):
    __tablename__ = 'anchor_data_day'

    uin = db.Column(db.Integer, primary_key=True, nullable=False)
    add_date = db.Column(db.Date, primary_key=True, nullable=False)
    enter_amount = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    look_amount = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    enter_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    beat_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    fans_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_duration = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_award = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    watch_award = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    active_award = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    basic_award = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    enter_ver_pv = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    out_ver_pv = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    enter_uv = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    look_uv = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    out_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    talk_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class AnchorDataDetail(db.Model):
    __tablename__ = 'anchor_data_detail'

    uin = db.Column(db.Integer, primary_key=True, nullable=False)
    vid = db.Column(db.String(32), primary_key=True, nullable=False)
    add_date = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    fans_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_duration = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_award = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    watch_award = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    active_award = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    start_fans_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    end_fans_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    same_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    diff_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    only_talk = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    new_user = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    hot_score = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BltTaskRewardTbl(db.Model):
    __tablename__ = 'blt_task_reward_tbl'
    __table_args__ = (
        db.Index('idx_uin_task_id', 'uin', 'task_id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    gold = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    power = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    foreign_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status_gold = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status_power = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    gold_get_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    power_get_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


t_bo_ad_visiturl = db.Table(
    'bo_ad_visiturl',
    db.Column('tjdate', db.Date, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('systype', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('add_time', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('ip', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Index('tjdate_flag', 'tjdate', 'flag', 'symbol')
)


class BoAdVisiturlAnalysi(db.Model):
    __tablename__ = 'bo_ad_visiturl_analysis'

    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    systype = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    show_pv = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    show_uv = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    click_pv = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    click_uv = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    download_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    login_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue())


class BoAuthOriginDuplicate(db.Model):
    __tablename__ = 'bo_auth_origin_duplicate'
    __table_args__ = (
        db.Index('uin_live_pid', 'uin', 'uin_live', 'pid'),
    )

    mac = db.Column(db.String(32), primary_key=True, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    block = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    logintime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    loginnum = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    source = db.Column(db.String(32), server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoAuthOriginDuplicateTow(db.Model):
    __tablename__ = 'bo_auth_origin_duplicate_tow'

    uin_live = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, index=True, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    year_week = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    block = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    live_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    live_time_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sent = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sent_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_num_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_auth = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_auth_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_mac = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_mac_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    sent_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    song_sent = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    song_sent_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    song_sent_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    light_sent_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    light_sent = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    blt_sent = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    blt_sent_xp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


t_bo_auth_origin_info = db.Table(
    'bo_auth_origin_info',
    db.Column('uin', db.Integer, nullable=False, unique=True, server_default=db.FetchedValue()),
    db.Column('auth_origin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin_live', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('pid', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('oprtime', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('authnum', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('logintime', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('loginnum', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('source', db.String(32), server_default=db.FetchedValue()),
    db.Column('mac', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('channels', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('flag_dup', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Index('uin_live', 'uin_live', 'pid')
)


class BoBannerInfo(db.Model):
    __tablename__ = 'bo_banner_info'

    id = db.Column(db.Integer, primary_key=True)
    lt_pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    types = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    opr_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    imgurl = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue())
    special_content = db.Column(db.Text)
    special_url = db.Column(db.Text)
    expiretime = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    opruser = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    ip = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    mac = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())


class BoBannerParticipant(db.Model):
    __tablename__ = 'bo_banner_participants'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    banner_id = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    block = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    reason = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    opr_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    active_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    opruser = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    visit_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoBlackInfo(db.Model):
    __tablename__ = 'bo_black_info'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    blackuin = db.Column(db.Integer, primary_key=True, nullable=False, index=True, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoCarouselInfo(db.Model):
    __tablename__ = 'bo_carousel_info'

    id = db.Column(db.Integer, primary_key=True)
    lt_pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    msg = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue())
    opr_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoCashAssignment(db.Model):
    __tablename__ = 'bo_cash_assignment'
    __table_args__ = (
        db.Index('uin', 'uin', 'rid', 'pid', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    rid = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    been_view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoCashViewTime(db.Model):
    __tablename__ = 'bo_cash_view_time'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    been_view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    been_view_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoConfigAward(db.Model):
    __tablename__ = 'bo_config_award'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    year_week = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_duration_min = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_day_max = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoConfigIntegralTbl(db.Model):
    __tablename__ = 'bo_config_integral_tbl'

    pid = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    live_time_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    live_award_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    live_award_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    view_award_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    view_award_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    watch_time_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    watch_award_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    watch_award_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    gift_time_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    gift_award_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    gift_award_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_award_auth = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_award_mac = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_award_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    song_time_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    song_award_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    song_award_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoConfigTbl(db.Model):
    __tablename__ = 'bo_config_tbl'

    pid = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    prorate_quo = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    datacard = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    apart_time = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    share_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vedio_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vedio_award_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vedio_time_limit = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    red_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    red_expire = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    red_award_down = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    red_award_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    red_rate_0 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    red_rate_1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    red_rate_2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    red_rate_3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort_top = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort_review = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_red = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_switch_detail = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_switch_view = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_withdraw = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_spread_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_spread_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_red_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_red_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_spread_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_upper_num = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rate1 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rate2 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rate3 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rate4 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rate5 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rate_sales = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rs1 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rs2 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rs3 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rs4 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_rate_out = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_switch_cash = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_rate_view = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_rand_time = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_cap_mon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_cap_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_ios_spread_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_ios_spread_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_ios_red_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_ios_red_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ds_ios_rate1 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rate2 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rate3 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rate4 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rate5 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rate_sales = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rs1 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rs2 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rs3 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    ds_ios_rs4 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    newuser_reward_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    newuser_view_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    newuser_view_award_max = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    newuser_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    double_award_time_start = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    double_award_time_end = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    olderuser_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_livetime_need = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_receive_need = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    exp_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    exp_live_max = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    exp_view = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    exp_view_max = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    exp_login_json = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    exp_share = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    exp_share_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    exp_chat_msg = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    exp_chat_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


t_bo_cooperative_channel = db.Table(
    'bo_cooperative_channel',
    db.Column('client_channel', db.String(64), unique=True),
    db.Column('marknum', db.SmallInteger, nullable=False, unique=True, server_default=db.FetchedValue()),
    db.Column('add_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('memo', db.String(128), nullable=False, server_default=db.FetchedValue())
)


class BoDsAwardMac(db.Model):
    __tablename__ = 'bo_ds_award_mac'

    mac = db.Column(db.String(64), primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoDsLevelSale(db.Model):
    __tablename__ = 'bo_ds_level_sales'

    levels = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    level_sales = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    level_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperChargeDay(db.Model):
    __tablename__ = 'bo_ds_super_charge_day'
    __table_args__ = (
        db.Index('uin_pid', 'uin', 'pid', 'tjdate'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    uin_src = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_money = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201602(db.Model):
    __tablename__ = 'bo_ds_super_pay_201602'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201603(db.Model):
    __tablename__ = 'bo_ds_super_pay_201603'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201604(db.Model):
    __tablename__ = 'bo_ds_super_pay_201604'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201605(db.Model):
    __tablename__ = 'bo_ds_super_pay_201605'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201606(db.Model):
    __tablename__ = 'bo_ds_super_pay_201606'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201607(db.Model):
    __tablename__ = 'bo_ds_super_pay_201607'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201608(db.Model):
    __tablename__ = 'bo_ds_super_pay_201608'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201609(db.Model):
    __tablename__ = 'bo_ds_super_pay_201609'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201610(db.Model):
    __tablename__ = 'bo_ds_super_pay_201610'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201611(db.Model):
    __tablename__ = 'bo_ds_super_pay_201611'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201612(db.Model):
    __tablename__ = 'bo_ds_super_pay_201612'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201701(db.Model):
    __tablename__ = 'bo_ds_super_pay_201701'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201702(db.Model):
    __tablename__ = 'bo_ds_super_pay_201702'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201703(db.Model):
    __tablename__ = 'bo_ds_super_pay_201703'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201704(db.Model):
    __tablename__ = 'bo_ds_super_pay_201704'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201705(db.Model):
    __tablename__ = 'bo_ds_super_pay_201705'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201706(db.Model):
    __tablename__ = 'bo_ds_super_pay_201706'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201707(db.Model):
    __tablename__ = 'bo_ds_super_pay_201707'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201708(db.Model):
    __tablename__ = 'bo_ds_super_pay_201708'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201709(db.Model):
    __tablename__ = 'bo_ds_super_pay_201709'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201710(db.Model):
    __tablename__ = 'bo_ds_super_pay_201710'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201711(db.Model):
    __tablename__ = 'bo_ds_super_pay_201711'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201712(db.Model):
    __tablename__ = 'bo_ds_super_pay_201712'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201801(db.Model):
    __tablename__ = 'bo_ds_super_pay_201801'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201802(db.Model):
    __tablename__ = 'bo_ds_super_pay_201802'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201803(db.Model):
    __tablename__ = 'bo_ds_super_pay_201803'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201804(db.Model):
    __tablename__ = 'bo_ds_super_pay_201804'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201805(db.Model):
    __tablename__ = 'bo_ds_super_pay_201805'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201806(db.Model):
    __tablename__ = 'bo_ds_super_pay_201806'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPay201807(db.Model):
    __tablename__ = 'bo_ds_super_pay_201807'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperPayBase(db.Model):
    __tablename__ = 'bo_ds_super_pay_base'
    __table_args__ = (
        db.Index('uin_flag', 'uin1', 'uin2', 'uin3', 'uin4', 'reward_flag', 'mark'),
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay_all = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_all = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    pay_sup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    rate_sup = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    reward_finish = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_leader = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    reward_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mark = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperUpgrade(db.Model):
    __tablename__ = 'bo_ds_super_upgrade'
    __table_args__ = (
        db.Index('flag_push_uin', 'flag_push', 'flag', 'uin', 'pid'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag_push = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    levels = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    level_rate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    payup = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperUserDay(db.Model):
    __tablename__ = 'bo_ds_super_user_day'
    __table_args__ = (
        db.Index('uin_pid', 'uin', 'pid', 'tjdate'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    uin_level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_src = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoDsSuperUserNumDay(db.Model):
    __tablename__ = 'bo_ds_super_user_num_day'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    num_day = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    num_all = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    red_reward = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoDsSuperiorUser(db.Model):
    __tablename__ = 'bo_ds_superior_user'
    __table_args__ = (
        db.Index('pid', 'pid', 'flag'),
        db.Index('uin1', 'uin1', 'uin2', 'uin3', 'uin4'),
        db.Index('logintype', 'logintype', 'flag')
    )

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pay0 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay1 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay2 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay3 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    pay4 = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    logintype = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    spread_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    reward0 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    reward1 = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    reward2 = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    reward3 = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    reward4 = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    flag_out = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    num1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    num2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    num3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    num4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    numall1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    numall2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    numall3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    numall4 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    depthline = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    depthnum = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    redtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    relation_award = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    mobile_mach = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


t_bo_fenx_award = db.Table(
    'bo_fenx_award',
    db.Column('qrcid', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('openid', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('lt_pid', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('lt_uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('amount', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('tjdate', db.Date, nullable=False, server_default=db.FetchedValue()),
    db.Column('hid', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Index('qrcid_openid', 'qrcid', 'openid')
)


class BoFenxHist(db.Model):
    __tablename__ = 'bo_fenx_hist'
    __table_args__ = (
        db.Index('openid_time', 'openid', 'createtime'),
    )

    hid = db.Column(db.Integer, primary_key=True)
    qrcid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    acid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    qid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    openid = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    qtype = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    createtime = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoFenxQrcode(db.Model):
    __tablename__ = 'bo_fenx_qrcode'
    __table_args__ = (
        db.Index('lt_pid_uin', 'lt_pid', 'lt_uin'),
    )

    qid = db.Column(db.Integer, primary_key=True)
    qrcid = db.Column(db.Integer, nullable=False, unique=True, server_default=db.FetchedValue())
    qname = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    model = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    fx_merchant = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    fx_scan = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lt_pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lt_uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    createtime = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoFundflowInfo(db.Model):
    __tablename__ = 'bo_fundflow_info'
    __table_args__ = (
        db.Index('uin_oprtime', 'uin', 'pid', 'oprtime', 'kind'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    dst = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    oprmoney = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    money = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    opr = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    memo = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())


class BoLiveConditionInfo(db.Model):
    __tablename__ = 'bo_live_condition_info'
    __table_args__ = (
        db.Index('uin_pid', 'uin', 'pid'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    net_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    frame_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoMoonApplyTbl(db.Model):
    __tablename__ = 'bo_moon_apply_tbl'

    uin = db.Column(db.Integer, primary_key=True, nullable=False)
    tel = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    talent_type = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime)


class BoOperateConfig(db.Model):
    __tablename__ = 'bo_operate_config'

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    award_flag = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    basic_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    basic_lower_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    basic_award_limit = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    basic_live_rate = db.Column(db.Float(10), nullable=False, server_default=db.FetchedValue())
    basic_award_rate = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    view_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_lower_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_upper_limit = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_upper_all = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_award = db.Column(db.Float(10), nullable=False, server_default=db.FetchedValue())
    view_baodi_award = db.Column(db.Float(10), nullable=False, server_default=db.FetchedValue())
    view_baodi_time = db.Column(db.Float(10), nullable=False, server_default=db.FetchedValue())
    view_award_rate = db.Column(db.Float(10), nullable=False, server_default=db.FetchedValue())
    view_baodi_upper = db.Column(db.Float(10), nullable=False, server_default=db.FetchedValue())
    share_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_num_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_platform = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue())
    share_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    give_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    give_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    give_num_upper = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    give_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    give_platform = db.Column(db.String(1024), nullable=False, server_default=db.FetchedValue())
    premiere_switch = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    premiere_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    premiere_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_duration_min = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_day_max = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoOprDataMin(db.Model):
    __tablename__ = 'bo_opr_data_min'

    id = db.Column(db.Integer, primary_key=True)
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    live_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    finish_vid_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    active_vid_uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    active_view_uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    per_vid_view_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    max_view_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mid_view_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mid_view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    error_vid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    per_chat_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoPayAccount(db.Model):
    __tablename__ = 'bo_pay_account'

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    realname = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    alipay = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    paypal = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    pay_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoPopupMacInfo(db.Model):
    __tablename__ = 'bo_popup_mac_info'

    mac = db.Column(db.String(64), primary_key=True, server_default=db.FetchedValue())
    settime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoReceivedFlow(db.Model):
    __tablename__ = 'bo_received_flow'
    __table_args__ = (
        db.Index('pid', 'pid', 'uin'),
    )

    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, nullable=False)
    uin = db.Column(db.Integer, nullable=False)
    oprcash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    oprreceived = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    dealtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, nullable=False, index=True, server_default=db.FetchedValue())
    memo = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    pay_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    oprname = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    examine_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    live_not = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    condition_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordAll(db.Model):
    __tablename__ = 'bo_record_all'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201508(db.Model):
    __tablename__ = 'bo_record_day_201508'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201509(db.Model):
    __tablename__ = 'bo_record_day_201509'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201510(db.Model):
    __tablename__ = 'bo_record_day_201510'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201511(db.Model):
    __tablename__ = 'bo_record_day_201511'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201512(db.Model):
    __tablename__ = 'bo_record_day_201512'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201601(db.Model):
    __tablename__ = 'bo_record_day_201601'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201602(db.Model):
    __tablename__ = 'bo_record_day_201602'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201603(db.Model):
    __tablename__ = 'bo_record_day_201603'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201604(db.Model):
    __tablename__ = 'bo_record_day_201604'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201605(db.Model):
    __tablename__ = 'bo_record_day_201605'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201606(db.Model):
    __tablename__ = 'bo_record_day_201606'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201607(db.Model):
    __tablename__ = 'bo_record_day_201607'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201608(db.Model):
    __tablename__ = 'bo_record_day_201608'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201609(db.Model):
    __tablename__ = 'bo_record_day_201609'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201610(db.Model):
    __tablename__ = 'bo_record_day_201610'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201611(db.Model):
    __tablename__ = 'bo_record_day_201611'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201612(db.Model):
    __tablename__ = 'bo_record_day_201612'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201701(db.Model):
    __tablename__ = 'bo_record_day_201701'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201702(db.Model):
    __tablename__ = 'bo_record_day_201702'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201703(db.Model):
    __tablename__ = 'bo_record_day_201703'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201704(db.Model):
    __tablename__ = 'bo_record_day_201704'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201705(db.Model):
    __tablename__ = 'bo_record_day_201705'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201706(db.Model):
    __tablename__ = 'bo_record_day_201706'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201707(db.Model):
    __tablename__ = 'bo_record_day_201707'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201708(db.Model):
    __tablename__ = 'bo_record_day_201708'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201709(db.Model):
    __tablename__ = 'bo_record_day_201709'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201710(db.Model):
    __tablename__ = 'bo_record_day_201710'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201711(db.Model):
    __tablename__ = 'bo_record_day_201711'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201712(db.Model):
    __tablename__ = 'bo_record_day_201712'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201801(db.Model):
    __tablename__ = 'bo_record_day_201801'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201802(db.Model):
    __tablename__ = 'bo_record_day_201802'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201803(db.Model):
    __tablename__ = 'bo_record_day_201803'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201804(db.Model):
    __tablename__ = 'bo_record_day_201804'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201805(db.Model):
    __tablename__ = 'bo_record_day_201805'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201806(db.Model):
    __tablename__ = 'bo_record_day_201806'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDay201807(db.Model):
    __tablename__ = 'bo_record_day_201807'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordDayBase(db.Model):
    __tablename__ = 'bo_record_day_base'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordHist(db.Model):
    __tablename__ = 'bo_record_hist'

    symbol = db.Column(db.String(64), primary_key=True, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    new_date = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())


t_bo_record_hist_201508 = db.Table(
    'bo_record_hist_201508',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201509 = db.Table(
    'bo_record_hist_201509',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201510 = db.Table(
    'bo_record_hist_201510',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201511 = db.Table(
    'bo_record_hist_201511',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201512 = db.Table(
    'bo_record_hist_201512',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201601 = db.Table(
    'bo_record_hist_201601',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201602 = db.Table(
    'bo_record_hist_201602',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201603 = db.Table(
    'bo_record_hist_201603',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201604 = db.Table(
    'bo_record_hist_201604',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201605 = db.Table(
    'bo_record_hist_201605',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201606 = db.Table(
    'bo_record_hist_201606',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201607 = db.Table(
    'bo_record_hist_201607',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201608 = db.Table(
    'bo_record_hist_201608',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201609 = db.Table(
    'bo_record_hist_201609',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201610 = db.Table(
    'bo_record_hist_201610',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201611 = db.Table(
    'bo_record_hist_201611',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201612 = db.Table(
    'bo_record_hist_201612',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201701 = db.Table(
    'bo_record_hist_201701',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201702 = db.Table(
    'bo_record_hist_201702',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201703 = db.Table(
    'bo_record_hist_201703',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201704 = db.Table(
    'bo_record_hist_201704',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201705 = db.Table(
    'bo_record_hist_201705',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201706 = db.Table(
    'bo_record_hist_201706',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201707 = db.Table(
    'bo_record_hist_201707',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201708 = db.Table(
    'bo_record_hist_201708',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201709 = db.Table(
    'bo_record_hist_201709',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201710 = db.Table(
    'bo_record_hist_201710',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201711 = db.Table(
    'bo_record_hist_201711',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201712 = db.Table(
    'bo_record_hist_201712',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201801 = db.Table(
    'bo_record_hist_201801',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201802 = db.Table(
    'bo_record_hist_201802',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201803 = db.Table(
    'bo_record_hist_201803',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201804 = db.Table(
    'bo_record_hist_201804',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201805 = db.Table(
    'bo_record_hist_201805',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201806 = db.Table(
    'bo_record_hist_201806',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_201807 = db.Table(
    'bo_record_hist_201807',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


t_bo_record_hist_base = db.Table(
    'bo_record_hist_base',
    db.Column('vid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('classify', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('device_type_quo', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('visit_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Column('origin_url', db.String(255), nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time_symbol', 'vid', 'uin', 'visit_time', 'symbol', 'classify')
)


class BoRecordMon201508(db.Model):
    __tablename__ = 'bo_record_mon_201508'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201509(db.Model):
    __tablename__ = 'bo_record_mon_201509'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201510(db.Model):
    __tablename__ = 'bo_record_mon_201510'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201511(db.Model):
    __tablename__ = 'bo_record_mon_201511'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201512(db.Model):
    __tablename__ = 'bo_record_mon_201512'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201601(db.Model):
    __tablename__ = 'bo_record_mon_201601'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201602(db.Model):
    __tablename__ = 'bo_record_mon_201602'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201603(db.Model):
    __tablename__ = 'bo_record_mon_201603'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201604(db.Model):
    __tablename__ = 'bo_record_mon_201604'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201605(db.Model):
    __tablename__ = 'bo_record_mon_201605'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201606(db.Model):
    __tablename__ = 'bo_record_mon_201606'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201607(db.Model):
    __tablename__ = 'bo_record_mon_201607'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201608(db.Model):
    __tablename__ = 'bo_record_mon_201608'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201609(db.Model):
    __tablename__ = 'bo_record_mon_201609'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201610(db.Model):
    __tablename__ = 'bo_record_mon_201610'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201611(db.Model):
    __tablename__ = 'bo_record_mon_201611'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201612(db.Model):
    __tablename__ = 'bo_record_mon_201612'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201701(db.Model):
    __tablename__ = 'bo_record_mon_201701'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201702(db.Model):
    __tablename__ = 'bo_record_mon_201702'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201703(db.Model):
    __tablename__ = 'bo_record_mon_201703'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201704(db.Model):
    __tablename__ = 'bo_record_mon_201704'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201705(db.Model):
    __tablename__ = 'bo_record_mon_201705'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201706(db.Model):
    __tablename__ = 'bo_record_mon_201706'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201707(db.Model):
    __tablename__ = 'bo_record_mon_201707'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201708(db.Model):
    __tablename__ = 'bo_record_mon_201708'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201709(db.Model):
    __tablename__ = 'bo_record_mon_201709'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201710(db.Model):
    __tablename__ = 'bo_record_mon_201710'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201711(db.Model):
    __tablename__ = 'bo_record_mon_201711'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201712(db.Model):
    __tablename__ = 'bo_record_mon_201712'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201801(db.Model):
    __tablename__ = 'bo_record_mon_201801'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201802(db.Model):
    __tablename__ = 'bo_record_mon_201802'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201803(db.Model):
    __tablename__ = 'bo_record_mon_201803'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201804(db.Model):
    __tablename__ = 'bo_record_mon_201804'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201805(db.Model):
    __tablename__ = 'bo_record_mon_201805'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201806(db.Model):
    __tablename__ = 'bo_record_mon_201806'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMon201807(db.Model):
    __tablename__ = 'bo_record_mon_201807'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRecordMonBase(db.Model):
    __tablename__ = 'bo_record_mon_base'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    classify = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    origin_wx = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_qq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    origin_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_pc = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_ios = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_android = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    device_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoRedAwardHist(db.Model):
    __tablename__ = 'bo_red_award_hist'
    __table_args__ = (
        db.Index('share_uin', 'share_level', 'uin', 'lt_uin', 'lt_pid'),
    )

    id = db.Column(db.Integer, primary_key=True)
    share_level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lt_uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lt_pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_money = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


t_bo_red_share_ties = db.Table(
    'bo_red_share_ties',
    db.Column('lt_uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('lt_pid', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin1', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin2', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin3', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin4', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('red_money', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('awardall_0', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('awardall_1', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('awardall_2', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('awardall_3', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin1_num', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin2_num', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin3_num', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag1', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag2', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag3', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('follow_status', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('use_status', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('add_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('depthline', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('depthnum', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('award_json', db.String(128), nullable=False, server_default=db.FetchedValue()),
    db.Index('uin_pid', 'lt_uin', 'lt_pid')
)


t_bo_redwx_order = db.Table(
    'bo_redwx_order',
    db.Column('mch_billno', db.String(32), nullable=False, unique=True, server_default=db.FetchedValue()),
    db.Column('mch_id', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('re_openid', db.String(32), nullable=False, server_default=db.FetchedValue()),
    db.Column('total_amount', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('send_time', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('send_listid', db.String(32), nullable=False, server_default=db.FetchedValue())
)


class BoReviewUser(db.Model):
    __tablename__ = 'bo_review_user'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    review_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    review_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoReviewVedio(db.Model):
    __tablename__ = 'bo_review_vedio'
    __table_args__ = (
        db.Index('vid_uin_pid', 'vid', 'uin', 'pid'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoReviewVedioHist(db.Model):
    __tablename__ = 'bo_review_vedio_hist'
    __table_args__ = (
        db.Index('vid_uin_pid', 'vid', 'uin', 'pid'),
    )

    symbol = db.Column(db.String(64), primary_key=True, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoSchoolIdentity(db.Model):
    __tablename__ = 'bo_school_identity'

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, index=True)
    xb_level = db.Column(db.Integer, nullable=False)
    js_level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoShareAwardAnchor(db.Model):
    __tablename__ = 'bo_share_award_anchor'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    award_times = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    share_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoShareAwardTime(db.Model):
    __tablename__ = 'bo_share_award_times'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    platform = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    award_times = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    share_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoShareAwardTimesMac(db.Model):
    __tablename__ = 'bo_share_award_times_mac'

    mac = db.Column(db.String(64), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    platform = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    award_times = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    share_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoShareAwardUser(db.Model):
    __tablename__ = 'bo_share_award_user'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    award_times = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    share_award = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoShareExtend(db.Model):
    __tablename__ = 'bo_share_extend'
    __table_args__ = (
        db.Index('vid_share', 'share_time', 'flag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    share_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    source = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    inside = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    shareuin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    symbol = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    share_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())


t_bo_share_info = db.Table(
    'bo_share_info',
    db.Column('vid', db.String(32), nullable=False, index=True, server_default=db.FetchedValue()),
    db.Column('share_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Column('flag', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('source', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('inside', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('pid', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('shareuin', db.Integer, nullable=False, index=True, server_default=db.FetchedValue()),
    db.Column('symbol', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('share_url', db.String(255), nullable=False, server_default=db.FetchedValue())
)


class BoShareOnlyurl(db.Model):
    __tablename__ = 'bo_share_onlyurl'

    symbol = db.Column(db.String(64), primary_key=True, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    shareuin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    new_date = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class BoSuggestInfo(db.Model):
    __tablename__ = 'bo_suggest_info'

    id = db.Column(db.Integer, primary_key=True)
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lt_uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    lt_pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    contact_info = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    url = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    extended = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())


class BoSumall(db.Model):
    __tablename__ = 'bo_sumall'
    __table_args__ = (
        db.Index('srcuin', 'srcuin', 'kind'),
    )

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, index=True, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201509(db.Model):
    __tablename__ = 'bo_sumday_201509'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False)
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201510(db.Model):
    __tablename__ = 'bo_sumday_201510'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False)
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201511(db.Model):
    __tablename__ = 'bo_sumday_201511'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201512(db.Model):
    __tablename__ = 'bo_sumday_201512'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201601(db.Model):
    __tablename__ = 'bo_sumday_201601'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201602(db.Model):
    __tablename__ = 'bo_sumday_201602'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201603(db.Model):
    __tablename__ = 'bo_sumday_201603'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201604(db.Model):
    __tablename__ = 'bo_sumday_201604'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201605(db.Model):
    __tablename__ = 'bo_sumday_201605'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201606(db.Model):
    __tablename__ = 'bo_sumday_201606'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201607(db.Model):
    __tablename__ = 'bo_sumday_201607'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201608(db.Model):
    __tablename__ = 'bo_sumday_201608'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201609(db.Model):
    __tablename__ = 'bo_sumday_201609'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, index=True, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201610(db.Model):
    __tablename__ = 'bo_sumday_201610'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201611(db.Model):
    __tablename__ = 'bo_sumday_201611'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201612(db.Model):
    __tablename__ = 'bo_sumday_201612'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201701(db.Model):
    __tablename__ = 'bo_sumday_201701'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201702(db.Model):
    __tablename__ = 'bo_sumday_201702'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201703(db.Model):
    __tablename__ = 'bo_sumday_201703'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201704(db.Model):
    __tablename__ = 'bo_sumday_201704'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201705(db.Model):
    __tablename__ = 'bo_sumday_201705'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201706(db.Model):
    __tablename__ = 'bo_sumday_201706'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201707(db.Model):
    __tablename__ = 'bo_sumday_201707'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201708(db.Model):
    __tablename__ = 'bo_sumday_201708'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201709(db.Model):
    __tablename__ = 'bo_sumday_201709'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201710(db.Model):
    __tablename__ = 'bo_sumday_201710'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201711(db.Model):
    __tablename__ = 'bo_sumday_201711'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201712(db.Model):
    __tablename__ = 'bo_sumday_201712'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201801(db.Model):
    __tablename__ = 'bo_sumday_201801'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201802(db.Model):
    __tablename__ = 'bo_sumday_201802'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201803(db.Model):
    __tablename__ = 'bo_sumday_201803'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201804(db.Model):
    __tablename__ = 'bo_sumday_201804'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201805(db.Model):
    __tablename__ = 'bo_sumday_201805'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201806(db.Model):
    __tablename__ = 'bo_sumday_201806'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumday201807(db.Model):
    __tablename__ = 'bo_sumday_201807'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayBase(db.Model):
    __tablename__ = 'bo_sumday_base'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201504(db.Model):
    __tablename__ = 'bo_sumdayvid_201504'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201505(db.Model):
    __tablename__ = 'bo_sumdayvid_201505'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201506(db.Model):
    __tablename__ = 'bo_sumdayvid_201506'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201507(db.Model):
    __tablename__ = 'bo_sumdayvid_201507'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201508(db.Model):
    __tablename__ = 'bo_sumdayvid_201508'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201509(db.Model):
    __tablename__ = 'bo_sumdayvid_201509'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201510(db.Model):
    __tablename__ = 'bo_sumdayvid_201510'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201511(db.Model):
    __tablename__ = 'bo_sumdayvid_201511'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201512(db.Model):
    __tablename__ = 'bo_sumdayvid_201512'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201601(db.Model):
    __tablename__ = 'bo_sumdayvid_201601'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201602(db.Model):
    __tablename__ = 'bo_sumdayvid_201602'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201603(db.Model):
    __tablename__ = 'bo_sumdayvid_201603'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201604(db.Model):
    __tablename__ = 'bo_sumdayvid_201604'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201605(db.Model):
    __tablename__ = 'bo_sumdayvid_201605'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201606(db.Model):
    __tablename__ = 'bo_sumdayvid_201606'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201607(db.Model):
    __tablename__ = 'bo_sumdayvid_201607'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201608(db.Model):
    __tablename__ = 'bo_sumdayvid_201608'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201609(db.Model):
    __tablename__ = 'bo_sumdayvid_201609'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201610(db.Model):
    __tablename__ = 'bo_sumdayvid_201610'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201611(db.Model):
    __tablename__ = 'bo_sumdayvid_201611'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201612(db.Model):
    __tablename__ = 'bo_sumdayvid_201612'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201701(db.Model):
    __tablename__ = 'bo_sumdayvid_201701'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201702(db.Model):
    __tablename__ = 'bo_sumdayvid_201702'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201703(db.Model):
    __tablename__ = 'bo_sumdayvid_201703'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201704(db.Model):
    __tablename__ = 'bo_sumdayvid_201704'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201705(db.Model):
    __tablename__ = 'bo_sumdayvid_201705'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201706(db.Model):
    __tablename__ = 'bo_sumdayvid_201706'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201707(db.Model):
    __tablename__ = 'bo_sumdayvid_201707'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201708(db.Model):
    __tablename__ = 'bo_sumdayvid_201708'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201709(db.Model):
    __tablename__ = 'bo_sumdayvid_201709'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201710(db.Model):
    __tablename__ = 'bo_sumdayvid_201710'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201711(db.Model):
    __tablename__ = 'bo_sumdayvid_201711'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201712(db.Model):
    __tablename__ = 'bo_sumdayvid_201712'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201801(db.Model):
    __tablename__ = 'bo_sumdayvid_201801'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201802(db.Model):
    __tablename__ = 'bo_sumdayvid_201802'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201803(db.Model):
    __tablename__ = 'bo_sumdayvid_201803'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201804(db.Model):
    __tablename__ = 'bo_sumdayvid_201804'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201805(db.Model):
    __tablename__ = 'bo_sumdayvid_201805'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201806(db.Model):
    __tablename__ = 'bo_sumdayvid_201806'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvid201807(db.Model):
    __tablename__ = 'bo_sumdayvid_201807'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvidBase(db.Model):
    __tablename__ = 'bo_sumdayvid_base'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumdayvidHistory(db.Model):
    __tablename__ = 'bo_sumdayvid_history'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201509(db.Model):
    __tablename__ = 'bo_summon_201509'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False)
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201510(db.Model):
    __tablename__ = 'bo_summon_201510'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False)
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201511(db.Model):
    __tablename__ = 'bo_summon_201511'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201512(db.Model):
    __tablename__ = 'bo_summon_201512'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201601(db.Model):
    __tablename__ = 'bo_summon_201601'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201602(db.Model):
    __tablename__ = 'bo_summon_201602'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201603(db.Model):
    __tablename__ = 'bo_summon_201603'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201604(db.Model):
    __tablename__ = 'bo_summon_201604'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201605(db.Model):
    __tablename__ = 'bo_summon_201605'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201606(db.Model):
    __tablename__ = 'bo_summon_201606'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201607(db.Model):
    __tablename__ = 'bo_summon_201607'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201608(db.Model):
    __tablename__ = 'bo_summon_201608'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201609(db.Model):
    __tablename__ = 'bo_summon_201609'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201610(db.Model):
    __tablename__ = 'bo_summon_201610'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201611(db.Model):
    __tablename__ = 'bo_summon_201611'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201612(db.Model):
    __tablename__ = 'bo_summon_201612'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201701(db.Model):
    __tablename__ = 'bo_summon_201701'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201702(db.Model):
    __tablename__ = 'bo_summon_201702'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201703(db.Model):
    __tablename__ = 'bo_summon_201703'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201704(db.Model):
    __tablename__ = 'bo_summon_201704'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201705(db.Model):
    __tablename__ = 'bo_summon_201705'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201706(db.Model):
    __tablename__ = 'bo_summon_201706'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201707(db.Model):
    __tablename__ = 'bo_summon_201707'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201708(db.Model):
    __tablename__ = 'bo_summon_201708'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201709(db.Model):
    __tablename__ = 'bo_summon_201709'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201710(db.Model):
    __tablename__ = 'bo_summon_201710'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201711(db.Model):
    __tablename__ = 'bo_summon_201711'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201712(db.Model):
    __tablename__ = 'bo_summon_201712'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201801(db.Model):
    __tablename__ = 'bo_summon_201801'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201802(db.Model):
    __tablename__ = 'bo_summon_201802'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201803(db.Model):
    __tablename__ = 'bo_summon_201803'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201804(db.Model):
    __tablename__ = 'bo_summon_201804'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201805(db.Model):
    __tablename__ = 'bo_summon_201805'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201806(db.Model):
    __tablename__ = 'bo_summon_201806'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummon201807(db.Model):
    __tablename__ = 'bo_summon_201807'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSummonBase(db.Model):
    __tablename__ = 'bo_summon_base'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatall(db.Model):
    __tablename__ = 'bo_sumstatall'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201510(db.Model):
    __tablename__ = 'bo_sumstatday_201510'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201511(db.Model):
    __tablename__ = 'bo_sumstatday_201511'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201512(db.Model):
    __tablename__ = 'bo_sumstatday_201512'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201601(db.Model):
    __tablename__ = 'bo_sumstatday_201601'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201602(db.Model):
    __tablename__ = 'bo_sumstatday_201602'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201603(db.Model):
    __tablename__ = 'bo_sumstatday_201603'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201604(db.Model):
    __tablename__ = 'bo_sumstatday_201604'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201605(db.Model):
    __tablename__ = 'bo_sumstatday_201605'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201606(db.Model):
    __tablename__ = 'bo_sumstatday_201606'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201607(db.Model):
    __tablename__ = 'bo_sumstatday_201607'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201608(db.Model):
    __tablename__ = 'bo_sumstatday_201608'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201609(db.Model):
    __tablename__ = 'bo_sumstatday_201609'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201610(db.Model):
    __tablename__ = 'bo_sumstatday_201610'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201611(db.Model):
    __tablename__ = 'bo_sumstatday_201611'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201612(db.Model):
    __tablename__ = 'bo_sumstatday_201612'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201701(db.Model):
    __tablename__ = 'bo_sumstatday_201701'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201702(db.Model):
    __tablename__ = 'bo_sumstatday_201702'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201703(db.Model):
    __tablename__ = 'bo_sumstatday_201703'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201704(db.Model):
    __tablename__ = 'bo_sumstatday_201704'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201705(db.Model):
    __tablename__ = 'bo_sumstatday_201705'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201706(db.Model):
    __tablename__ = 'bo_sumstatday_201706'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201707(db.Model):
    __tablename__ = 'bo_sumstatday_201707'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201708(db.Model):
    __tablename__ = 'bo_sumstatday_201708'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201709(db.Model):
    __tablename__ = 'bo_sumstatday_201709'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201710(db.Model):
    __tablename__ = 'bo_sumstatday_201710'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201711(db.Model):
    __tablename__ = 'bo_sumstatday_201711'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201712(db.Model):
    __tablename__ = 'bo_sumstatday_201712'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201801(db.Model):
    __tablename__ = 'bo_sumstatday_201801'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201802(db.Model):
    __tablename__ = 'bo_sumstatday_201802'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201803(db.Model):
    __tablename__ = 'bo_sumstatday_201803'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201804(db.Model):
    __tablename__ = 'bo_sumstatday_201804'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201805(db.Model):
    __tablename__ = 'bo_sumstatday_201805'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201806(db.Model):
    __tablename__ = 'bo_sumstatday_201806'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatday201807(db.Model):
    __tablename__ = 'bo_sumstatday_201807'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatdayBase(db.Model):
    __tablename__ = 'bo_sumstatday_base'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatmon201511(db.Model):
    __tablename__ = 'bo_sumstatmon_201511'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatmonAll(db.Model):
    __tablename__ = 'bo_sumstatmon_all'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatmonBase(db.Model):
    __tablename__ = 'bo_sumstatmon_base'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatweek201546(db.Model):
    __tablename__ = 'bo_sumstatweek_201546'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumstatweekBase(db.Model):
    __tablename__ = 'bo_sumstatweek_base'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201538(db.Model):
    __tablename__ = 'bo_sumweek_201538'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False)
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201539(db.Model):
    __tablename__ = 'bo_sumweek_201539'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False)
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201540(db.Model):
    __tablename__ = 'bo_sumweek_201540'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False)
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False)
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False)
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201541(db.Model):
    __tablename__ = 'bo_sumweek_201541'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201542(db.Model):
    __tablename__ = 'bo_sumweek_201542'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201543(db.Model):
    __tablename__ = 'bo_sumweek_201543'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201544(db.Model):
    __tablename__ = 'bo_sumweek_201544'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201545(db.Model):
    __tablename__ = 'bo_sumweek_201545'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201546(db.Model):
    __tablename__ = 'bo_sumweek_201546'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201547(db.Model):
    __tablename__ = 'bo_sumweek_201547'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201548(db.Model):
    __tablename__ = 'bo_sumweek_201548'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201549(db.Model):
    __tablename__ = 'bo_sumweek_201549'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201550(db.Model):
    __tablename__ = 'bo_sumweek_201550'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201551(db.Model):
    __tablename__ = 'bo_sumweek_201551'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201552(db.Model):
    __tablename__ = 'bo_sumweek_201552'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201601(db.Model):
    __tablename__ = 'bo_sumweek_201601'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201602(db.Model):
    __tablename__ = 'bo_sumweek_201602'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201603(db.Model):
    __tablename__ = 'bo_sumweek_201603'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201604(db.Model):
    __tablename__ = 'bo_sumweek_201604'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201605(db.Model):
    __tablename__ = 'bo_sumweek_201605'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201606(db.Model):
    __tablename__ = 'bo_sumweek_201606'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201607(db.Model):
    __tablename__ = 'bo_sumweek_201607'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201608(db.Model):
    __tablename__ = 'bo_sumweek_201608'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201609(db.Model):
    __tablename__ = 'bo_sumweek_201609'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201610(db.Model):
    __tablename__ = 'bo_sumweek_201610'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201611(db.Model):
    __tablename__ = 'bo_sumweek_201611'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201612(db.Model):
    __tablename__ = 'bo_sumweek_201612'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201613(db.Model):
    __tablename__ = 'bo_sumweek_201613'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201614(db.Model):
    __tablename__ = 'bo_sumweek_201614'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201615(db.Model):
    __tablename__ = 'bo_sumweek_201615'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201616(db.Model):
    __tablename__ = 'bo_sumweek_201616'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201617(db.Model):
    __tablename__ = 'bo_sumweek_201617'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201618(db.Model):
    __tablename__ = 'bo_sumweek_201618'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201619(db.Model):
    __tablename__ = 'bo_sumweek_201619'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201620(db.Model):
    __tablename__ = 'bo_sumweek_201620'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201621(db.Model):
    __tablename__ = 'bo_sumweek_201621'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201622(db.Model):
    __tablename__ = 'bo_sumweek_201622'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201623(db.Model):
    __tablename__ = 'bo_sumweek_201623'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201624(db.Model):
    __tablename__ = 'bo_sumweek_201624'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201625(db.Model):
    __tablename__ = 'bo_sumweek_201625'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201626(db.Model):
    __tablename__ = 'bo_sumweek_201626'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201627(db.Model):
    __tablename__ = 'bo_sumweek_201627'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201628(db.Model):
    __tablename__ = 'bo_sumweek_201628'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201629(db.Model):
    __tablename__ = 'bo_sumweek_201629'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201630(db.Model):
    __tablename__ = 'bo_sumweek_201630'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201631(db.Model):
    __tablename__ = 'bo_sumweek_201631'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201632(db.Model):
    __tablename__ = 'bo_sumweek_201632'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201633(db.Model):
    __tablename__ = 'bo_sumweek_201633'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201634(db.Model):
    __tablename__ = 'bo_sumweek_201634'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201635(db.Model):
    __tablename__ = 'bo_sumweek_201635'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201636(db.Model):
    __tablename__ = 'bo_sumweek_201636'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201637(db.Model):
    __tablename__ = 'bo_sumweek_201637'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201638(db.Model):
    __tablename__ = 'bo_sumweek_201638'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201639(db.Model):
    __tablename__ = 'bo_sumweek_201639'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201640(db.Model):
    __tablename__ = 'bo_sumweek_201640'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201642(db.Model):
    __tablename__ = 'bo_sumweek_201642'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201643(db.Model):
    __tablename__ = 'bo_sumweek_201643'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201644(db.Model):
    __tablename__ = 'bo_sumweek_201644'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201645(db.Model):
    __tablename__ = 'bo_sumweek_201645'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201646(db.Model):
    __tablename__ = 'bo_sumweek_201646'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201647(db.Model):
    __tablename__ = 'bo_sumweek_201647'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201648(db.Model):
    __tablename__ = 'bo_sumweek_201648'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201649(db.Model):
    __tablename__ = 'bo_sumweek_201649'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201702(db.Model):
    __tablename__ = 'bo_sumweek_201702'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201703(db.Model):
    __tablename__ = 'bo_sumweek_201703'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201704(db.Model):
    __tablename__ = 'bo_sumweek_201704'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201705(db.Model):
    __tablename__ = 'bo_sumweek_201705'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201706(db.Model):
    __tablename__ = 'bo_sumweek_201706'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201707(db.Model):
    __tablename__ = 'bo_sumweek_201707'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201708(db.Model):
    __tablename__ = 'bo_sumweek_201708'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201709(db.Model):
    __tablename__ = 'bo_sumweek_201709'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201710(db.Model):
    __tablename__ = 'bo_sumweek_201710'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201711(db.Model):
    __tablename__ = 'bo_sumweek_201711'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201712(db.Model):
    __tablename__ = 'bo_sumweek_201712'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201713(db.Model):
    __tablename__ = 'bo_sumweek_201713'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201714(db.Model):
    __tablename__ = 'bo_sumweek_201714'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201715(db.Model):
    __tablename__ = 'bo_sumweek_201715'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201716(db.Model):
    __tablename__ = 'bo_sumweek_201716'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201717(db.Model):
    __tablename__ = 'bo_sumweek_201717'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201718(db.Model):
    __tablename__ = 'bo_sumweek_201718'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201719(db.Model):
    __tablename__ = 'bo_sumweek_201719'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201720(db.Model):
    __tablename__ = 'bo_sumweek_201720'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201721(db.Model):
    __tablename__ = 'bo_sumweek_201721'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201722(db.Model):
    __tablename__ = 'bo_sumweek_201722'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201723(db.Model):
    __tablename__ = 'bo_sumweek_201723'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201724(db.Model):
    __tablename__ = 'bo_sumweek_201724'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201725(db.Model):
    __tablename__ = 'bo_sumweek_201725'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201726(db.Model):
    __tablename__ = 'bo_sumweek_201726'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201727(db.Model):
    __tablename__ = 'bo_sumweek_201727'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201728(db.Model):
    __tablename__ = 'bo_sumweek_201728'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201729(db.Model):
    __tablename__ = 'bo_sumweek_201729'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201730(db.Model):
    __tablename__ = 'bo_sumweek_201730'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201731(db.Model):
    __tablename__ = 'bo_sumweek_201731'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201732(db.Model):
    __tablename__ = 'bo_sumweek_201732'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201733(db.Model):
    __tablename__ = 'bo_sumweek_201733'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201734(db.Model):
    __tablename__ = 'bo_sumweek_201734'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201735(db.Model):
    __tablename__ = 'bo_sumweek_201735'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201736(db.Model):
    __tablename__ = 'bo_sumweek_201736'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201737(db.Model):
    __tablename__ = 'bo_sumweek_201737'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201738(db.Model):
    __tablename__ = 'bo_sumweek_201738'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201739(db.Model):
    __tablename__ = 'bo_sumweek_201739'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201740(db.Model):
    __tablename__ = 'bo_sumweek_201740'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201741(db.Model):
    __tablename__ = 'bo_sumweek_201741'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201742(db.Model):
    __tablename__ = 'bo_sumweek_201742'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201743(db.Model):
    __tablename__ = 'bo_sumweek_201743'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201744(db.Model):
    __tablename__ = 'bo_sumweek_201744'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201745(db.Model):
    __tablename__ = 'bo_sumweek_201745'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201746(db.Model):
    __tablename__ = 'bo_sumweek_201746'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201747(db.Model):
    __tablename__ = 'bo_sumweek_201747'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201748(db.Model):
    __tablename__ = 'bo_sumweek_201748'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201749(db.Model):
    __tablename__ = 'bo_sumweek_201749'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201750(db.Model):
    __tablename__ = 'bo_sumweek_201750'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201751(db.Model):
    __tablename__ = 'bo_sumweek_201751'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201752(db.Model):
    __tablename__ = 'bo_sumweek_201752'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201753(db.Model):
    __tablename__ = 'bo_sumweek_201753'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201801(db.Model):
    __tablename__ = 'bo_sumweek_201801'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201802(db.Model):
    __tablename__ = 'bo_sumweek_201802'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201803(db.Model):
    __tablename__ = 'bo_sumweek_201803'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201804(db.Model):
    __tablename__ = 'bo_sumweek_201804'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201805(db.Model):
    __tablename__ = 'bo_sumweek_201805'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201806(db.Model):
    __tablename__ = 'bo_sumweek_201806'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201807(db.Model):
    __tablename__ = 'bo_sumweek_201807'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201808(db.Model):
    __tablename__ = 'bo_sumweek_201808'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201809(db.Model):
    __tablename__ = 'bo_sumweek_201809'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201810(db.Model):
    __tablename__ = 'bo_sumweek_201810'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201811(db.Model):
    __tablename__ = 'bo_sumweek_201811'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201813(db.Model):
    __tablename__ = 'bo_sumweek_201813'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201814(db.Model):
    __tablename__ = 'bo_sumweek_201814'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201815(db.Model):
    __tablename__ = 'bo_sumweek_201815'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201816(db.Model):
    __tablename__ = 'bo_sumweek_201816'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201817(db.Model):
    __tablename__ = 'bo_sumweek_201817'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201818(db.Model):
    __tablename__ = 'bo_sumweek_201818'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201819(db.Model):
    __tablename__ = 'bo_sumweek_201819'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201820(db.Model):
    __tablename__ = 'bo_sumweek_201820'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201821(db.Model):
    __tablename__ = 'bo_sumweek_201821'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201822(db.Model):
    __tablename__ = 'bo_sumweek_201822'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201823(db.Model):
    __tablename__ = 'bo_sumweek_201823'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201824(db.Model):
    __tablename__ = 'bo_sumweek_201824'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201825(db.Model):
    __tablename__ = 'bo_sumweek_201825'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweek201826(db.Model):
    __tablename__ = 'bo_sumweek_201826'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoSumweekBase(db.Model):
    __tablename__ = 'bo_sumweek_base'

    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    kind = db.Column(db.SmallInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    amount = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    acash = db.Column(db.Float(15, True), nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoUserAwardReissue(db.Model):
    __tablename__ = 'bo_user_award_reissue'

    uin = db.Column(db.BigInteger, primary_key=True, nullable=False)
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    sentcount = db.Column(db.BigInteger)
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())


class BoUserConfig(db.Model):
    __tablename__ = 'bo_user_config'

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    sw_follow = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sw_play = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    dt_praise = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    praise_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    play_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    premiere_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    follow_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    use_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    join_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    active_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    active_ver = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserConfigHist(db.Model):
    __tablename__ = 'bo_user_config_hist'
    __table_args__ = (
        db.Index('pid_uin_time', 'pid', 'uin', 'add_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    play_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    oprname = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoUserFollow(db.Model):
    __tablename__ = 'bo_user_follow'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow1(db.Model):
    __tablename__ = 'bo_user_follow1'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow10(db.Model):
    __tablename__ = 'bo_user_follow10'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow2(db.Model):
    __tablename__ = 'bo_user_follow2'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow3(db.Model):
    __tablename__ = 'bo_user_follow3'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow4(db.Model):
    __tablename__ = 'bo_user_follow4'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow5(db.Model):
    __tablename__ = 'bo_user_follow5'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow6(db.Model):
    __tablename__ = 'bo_user_follow6'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow7(db.Model):
    __tablename__ = 'bo_user_follow7'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow8(db.Model):
    __tablename__ = 'bo_user_follow8'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollow9(db.Model):
    __tablename__ = 'bo_user_follow9'
    __table_args__ = (
        db.Index('pid_dstuin_addtime', 'dstuin', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    srcuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    dstuin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    token_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserFollowNum(db.Model):
    __tablename__ = 'bo_user_follow_num'

    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    uin = db.Column(db.Integer, primary_key=True, nullable=False)
    follow_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    fans_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserRecommend(db.Model):
    __tablename__ = 'bo_user_recommend'

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoUserZeroView(db.Model):
    __tablename__ = 'bo_user_zero_view'

    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    been_view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioComment(db.Model):
    __tablename__ = 'bo_vedio_comment'
    __table_args__ = (
        db.Index('vid_pid_time', 'vid', 'pid', 'vedio_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vedio_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    v_colour = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    v_comment = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    v_extend = db.Column(db.String(512), nullable=False, server_default=db.FetchedValue())


class BoVedioHistory(db.Model):
    __tablename__ = 'bo_vedio_history'
    __table_args__ = (
        db.Index('pid_index', 'pid', 'uin', 'flag', 'v_status', 'nominate', 'add_time'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, unique=True, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    nominate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    play_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    black_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_now = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_duration = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    praise_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    chat_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_lbs = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    v_address = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    v_content = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    topic = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    v_url = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    roomid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    serverid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    prgName = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    device_type_quo = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    view_num_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_now_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mac = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    ip = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    view_time_valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    live_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfo(db.Model):
    __tablename__ = 'bo_vedio_info'
    __table_args__ = (
        db.Index('pid_index', 'pid', 'uin'),
        db.Index('v_status', 'v_status', 'nominate')
    )

    id = db.Column(db.BigInteger, primary_key=True)
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, unique=True, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    nominate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    play_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    black_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    net_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    frame_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_now = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_duration = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    praise_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    chat_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_lbs = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    v_address = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    v_content = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    topic = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    v_url = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    roomid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    serverid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    prgName = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    device_type_quo = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    view_num_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_now_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mac = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    ip = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    view_time_valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    live_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    longitude = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue())
    latitude = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue())


t_bo_vedio_info_ext = db.Table(
    'bo_vedio_info_ext',
    db.Column('vid', db.String(32), nullable=False, unique=True, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('add_time', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('pid', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('share_wxpyq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('share_wxhy', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('share_qqkj', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('share_qqhy', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('share_wb', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('share_dzdp', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('share_rest', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('online_wxpyq', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('online_wxhy', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('online_qqkj', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('online_qqhy', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('online_wb', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('online_dzdp', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('online_rest', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Index('vid_uin_time', 'vid', 'uin', 'add_time')
)


class BoVedioInfoExtday201508(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201508'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201509(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201509'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201510(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201510'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201511(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201511'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201512(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201512'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201601(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201601'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201602(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201602'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201603(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201603'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201604(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201604'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201605(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201605'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201606(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201606'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201607(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201607'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201608(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201608'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201609(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201609'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201610(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201610'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201611(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201611'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201612(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201612'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201701(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201701'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201702(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201702'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201703(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201703'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201704(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201704'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201705(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201705'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201706(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201706'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201707(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201707'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201708(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201708'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201709(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201709'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201710(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201710'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201711(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201711'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201712(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201712'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201801(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201801'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201802(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201802'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201803(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201803'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201804(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201804'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201805(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201805'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201806(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201806'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtday201807(db.Model):
    __tablename__ = 'bo_vedio_info_extday_201807'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoExtdayBase(db.Model):
    __tablename__ = 'bo_vedio_info_extday_base'

    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    share_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxpyq = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wxhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqkj = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_qqhy = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_wb = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_dzdp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    online_rest = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoHist(db.Model):
    __tablename__ = 'bo_vedio_info_hist'

    id = db.Column(db.BigInteger, primary_key=True)
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    nominate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    play_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    black_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    net_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    frame_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_now = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_duration = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    praise_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    chat_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_lbs = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    v_address = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    v_content = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    topic = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    v_url = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    roomid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    serverid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    prgName = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    device_type_quo = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    view_num_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_now_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mac = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    ip = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    view_time_valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    live_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    opr_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioInfoHistory(db.Model):
    __tablename__ = 'bo_vedio_info_history'
    __table_args__ = (
        db.Index('v_status', 'v_status', 'nominate'),
        db.Index('pid_index', 'pid', 'uin')
    )

    id = db.Column(db.BigInteger, primary_key=True)
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, unique=True, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    nominate = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    play_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    award_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    black_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    net_status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    frame_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_now = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_duration = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    praise_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replay_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    chat_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    v_lbs = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    v_address = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    v_content = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    topic = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    v_url = db.Column(db.String(128), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    roomid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    serverid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    prgName = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    device_type_quo = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    marknum = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    view_num_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_now_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time_robot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mac = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    ip = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    view_time_valid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    live_num = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    longitude = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue())
    latitude = db.Column(db.Float(asdecimal=True), nullable=False, server_default=db.FetchedValue())


class BoVedioMac(db.Model):
    __tablename__ = 'bo_vedio_mac'

    tjdate = db.Column(db.Date, primary_key=True, nullable=False, server_default=db.FetchedValue())
    mac = db.Column(db.String(64), primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    v_duration_mac = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time_mac = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioReport(db.Model):
    __tablename__ = 'bo_vedio_report'
    __table_args__ = (
        db.Index('type_time', 'type_rp', 'add_time'),
    )

    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid_rp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_rp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    type_rp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    roomid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    content_deal = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    content_img = db.Column(db.String(256), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    award_type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201604(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201604'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201605(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201605'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201606(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201606'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201607(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201607'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201608(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201608'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201609(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201609'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201610(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201610'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201611(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201611'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201612(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201612'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201701(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201701'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201702(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201702'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201703(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201703'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201704(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201704'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201705(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201705'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201706(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201706'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201707(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201707'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201708(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201708'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201709(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201709'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201710(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201710'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201711(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201711'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201712(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201712'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201801(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201801'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201802(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201802'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201803(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201803'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201804(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201804'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201805(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201805'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201806(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201806'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHist201807(db.Model):
    __tablename__ = 'bo_vedio_view_hist_201807'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoVedioViewHistBase(db.Model):
    __tablename__ = 'bo_vedio_view_hist_base'
    __table_args__ = (
        db.Index('uin_pid_flag', 'uin', 'pid', 'yearmon', 'tjdate', 'flag'),
    )

    id = db.Column(db.BigInteger, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    yearmon = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_time = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_live = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    oprtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoWallInfo(db.Model):
    __tablename__ = 'bo_wall_info'
    __table_args__ = (
        db.Index('pid_flag', 'pid', 'flag'),
    )

    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    wall_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    oprname = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class BoWithdrawInfo(db.Model):
    __tablename__ = 'bo_withdraw_info'
    __table_args__ = (
        db.Index('uin_pid', 'uin', 'pid'),
        db.Index('source', 'source', 'open_id')
    )

    pay_tel = db.Column(db.BigInteger, primary_key=True, nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    pid = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    source = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    open_id = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


t_bo_withdraw_weixin = db.Table(
    'bo_withdraw_weixin',
    db.Column('unionid', db.String(64), nullable=False, server_default=db.FetchedValue()),
    db.Column('pay_tel', db.BigInteger, nullable=False, server_default=db.FetchedValue()),
    db.Column('uin', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('pid', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('source', db.Integer, nullable=False, server_default=db.FetchedValue()),
    db.Column('open_id', db.String(64), nullable=False, index=True, server_default=db.FetchedValue()),
    db.Column('add_time', db.DateTime, nullable=False, server_default=db.FetchedValue()),
    db.Index('unionid_pay', 'unionid', 'pay_tel'),
    db.Index('uin_pid', 'uin', 'pid')
)


class BrokerAwardDayTbl(db.Model):
    __tablename__ = 'broker_award_day_tbl'
    __table_args__ = (
        db.Index('uin_broker', 'uin_broker', 'uin_anchor', 'add_date'),
        db.Index('add_date', 'uin_broker', 'add_date')
    )

    id = db.Column(db.Integer, primary_key=True)
    uin_broker = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    uin_anchor = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    add_date = db.Column(db.Date, nullable=False, server_default=db.FetchedValue())
    received = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    level = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BrokerAwardTbl(db.Model):
    __tablename__ = 'broker_award_tbl'

    id = db.Column(db.Integer, primary_key=True)
    uin_broker = db.Column(db.Integer, nullable=False, unique=True)
    received = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    anchor_num1 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    anchor_num2 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    anchor_num3 = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class BrokerRelationTbl(db.Model):
    __tablename__ = 'broker_relation_tbl'

    uin = db.Column(db.Integer, primary_key=True)
    uin1 = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    uin2 = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    uin3 = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    add_time = db.Column(db.DateTime, nullable=False)


class EmojiAlbumTbl(db.Model):
    __tablename__ = 'emoji_album_tbl'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    gold = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue())
    surface_url = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    album_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class EmojiImageTbl(db.Model):
    __tablename__ = 'emoji_image_tbl'

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    album_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    image_a = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_o = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_width = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    image_height = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    hash_key = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    image_sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class EmojiMarketTbl(db.Model):
    __tablename__ = 'emoji_market_tbl'

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    order = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    click = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    like = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    dislike = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class EmojiOrderTbl(db.Model):
    __tablename__ = 'emoji_order_tbl'
    __table_args__ = (
        db.Index('uin', 'uin', 'album_id', 'status'),
    )

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    album_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class ExpLevelConfigTbl(db.Model):
    __tablename__ = 'exp_level_config_tbl'

    level = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    exp = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class ExpSignIn(db.Model):
    __tablename__ = 'exp_sign_in'

    uin = db.Column(db.Integer, primary_key=True)
    continue_days = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    total_days = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    last_sign_in_time = db.Column(db.DateTime, nullable=False)


class ImageTbl(db.Model):
    __tablename__ = 'image_tbl'

    id = db.Column(db.Integer, primary_key=True)
    image_o = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_a = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_b = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_c = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_d = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_g = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    image_width = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    image_height = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    hash_key = db.Column(db.String(40), nullable=False, index=True, server_default=db.FetchedValue())
    file_ext = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue())
    file_size = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    mime_type = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class MsgRoomTbl(db.Model):
    __tablename__ = 'msg_room_tbl'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    end_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.Text)
    kind = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    language = db.Column(db.String(16), server_default=db.FetchedValue())


class NewActiveTbl(db.Model):
    __tablename__ = 'new_active_tbl'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    start_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    end_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    need_gold = db.Column(db.Numeric(40, 20), nullable=False, server_default=db.FetchedValue())


class PrizeTbl(db.Model):
    __tablename__ = 'prize_tbl'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    prob = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue())
    curr_prob = db.Column(db.Numeric(5, 4), nullable=False, server_default=db.FetchedValue())
    activity_id = db.Column(db.Integer, nullable=False, index=True)
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    gold = db.Column(db.Numeric(40, 20), nullable=False, server_default=db.FetchedValue())
    img = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    sort = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class SongChooseTbl(db.Model):
    __tablename__ = 'song_choose_tbl'

    choose_id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    watch_uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    anchor_uin = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    money = db.Column(db.BigInteger, nullable=False)
    comment_star = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    add_time = db.Column(db.Integer, nullable=False)


class SongFeedbackTbl(db.Model):
    __tablename__ = 'song_feedback_tbl'

    id = db.Column(db.Integer, primary_key=True)
    error_codes = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    uin = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    vid = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    song_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    song_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    song_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    file_name = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    author_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    lyric = db.Column(db.Text)
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class SongGift(db.Model):
    __tablename__ = 'song_gift'

    uin = db.Column(db.Integer, primary_key=True)
    gift_1 = db.Column(db.BigInteger, nullable=False, server_default=db.FetchedValue())
    gift_2 = db.Column(db.BigInteger, nullable=False)
    gift_3 = db.Column(db.BigInteger, nullable=False)


class SongMenuTbl(db.Model):
    __tablename__ = 'song_menu_tbl'

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    song_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    song_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    file_name = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    author_name = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    lyric = db.Column(db.Text)
    flag = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    comment_star = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment_times = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    time_length = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class SumdayTmp(db.Model):
    __tablename__ = 'sumday_tmp'

    uin = db.Column(db.BigInteger, primary_key=True, nullable=False)
    kind = db.Column(db.Integer, primary_key=True, nullable=False, server_default=db.FetchedValue())
    tjdate = db.Column(db.Date, primary_key=True, nullable=False, index=True, server_default=db.FetchedValue())
    sentcount = db.Column(db.BigInteger)
    add_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class Test1(db.Model):
    __tablename__ = 'test1'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    time = db.Column(db.DateTime, primary_key=True, nullable=False, server_default=db.FetchedValue())


class Test2(db.Model):
    __tablename__ = 'test2'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    time = db.Column(db.DateTime, primary_key=True, nullable=False, server_default=db.FetchedValue())


class Test3(db.Model):
    __tablename__ = 'test3'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    time = db.Column(db.DateTime, primary_key=True, nullable=False, server_default=db.FetchedValue())


class TestUser(db.Model):
    __tablename__ = 'test_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


class TurnDrawLog(db.Model):
    __tablename__ = 'turn_draw_log'

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, index=True)
    prize_id = db.Column(db.Integer, nullable=False)
    addr_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    activity_id = db.Column(db.Integer, nullable=False)
    ip = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue())
    mac = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, index=True, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class UserReportTbl(db.Model):
    __tablename__ = 'user_report_tbl'

    id = db.Column(db.Integer, primary_key=True)
    uin = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    report_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue())
    type = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class WallTbl(db.Model):
    __tablename__ = 'wall_tbl'

    rank = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    icon_url = db.Column(db.String(100), nullable=False)
    skip_url = db.Column(db.String(100), nullable=False)
