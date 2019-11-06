import pymysql

class DBHelper:
    def __init__(self,params):
        self.conn = pymysql.Connect(**params)
        self.init_param()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    def init_param(self):
        self.params = {
            'fields':'*',
            'table':'',
            'where':'',
            'groupby':'',
            'having':'',
            'orderby':'',
            'limit':''
        }
    def where(self,**kwargs):
        ops = {
            'ne':'!=',
            'gt':'>',
            'ge':'>=',
            'lt':'<',
            'le':'<=',
            'contains':'like',
            'in':'in',
            'nin':'not in'
        }
        result = " where "
        for key in kwargs:
            keys = key.split("__")
            if len(key)>1:
                op = ops[keys[1]]
                if isinstance(kwargs[key],str):
                    result += keys[0] + op + "'" + kwargs[key] +"' and"
                else:
                    result += keys[0] + op +kwargs[key] + 'and'
            else:
                if isinstance(kwargs[key],str):
                    result += keys[0] + "= '" + kwargs[key] + "' and"
                else:
                    result += keys[0] + " = " + kwargs[key] + 'and'
        result = result.strip('and')
        self.params['where'] = result
        return  self
    def table(self,tables):
        self.params['tables'] = tables
        return self
    def fields(self,fields):
        self.params['fields'] = fields
        return self
    def select(self):
        sql = "select {fields} from {tables} {where} {groupby} {having} {orderby} {limit}"
        sql = sql.format(**self.params)
        print(sql)
        self.cursor.execute(sql)
        self.init_param()
        return self.cursor.fetchall()

if __name__ == '__main__':
    from settings import dbparams
    db = DBHelper(dbparams)
    date = db.table('user').fields('username,usertype,password,regtime,email').select()
    print(date)
