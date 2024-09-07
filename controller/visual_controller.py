from PySide2 import QtGui, QtCore
from PySide2.QtGui import QImage, QPixmap, QColor
from PySide2.QtWidgets import QFileDialog
import mysql.connector
db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root", 
    auth_plugin='mysql_native_password',
    password = "larrykuo01",
    database = "GameOfThrones"
)
mycursor = db.cursor()
class MainWindow():
    def __init__(self , ui):
        self.connect_ui()
        self.showMaximized()

        #Combo Box
        Choices = [
            "","SELECT", "UPDATE", "IN", "NOT IN", "EXISTS", "NOT EXISTS", "COUNT", "SUM", "MAX", "MIN", "AVG", "HAVING"
        ]
        self.ui.comboBox.addItems(Choices)
        self.ui.comboBox.currentIndexChanged.connect(self.Button)
    
    # 什麼widget要connect到哪個function寫在這邊
    def connect_ui(self):
        # button的長這樣
        self.ui.chracter_insert_pushButton.clicked.connect(self.InsertCharacter)
        self.ui.chracter_delete_pushButton.clicked.connect(self.DeleteCharacter)

        self.ui.player_insert_pushButton.clicked.connect(self.InsertPlayer)
        self.ui.player_delete_pushButton.clicked.connect(self.DeletePlayer)

        self.ui.war_insert_pushButton.clicked.connect(self.InsertWar)
        self.ui.war_delete_pushButton.clicked.connect(self.DeleteWar)

        self.ui.territory_insert_pushButton.clicked.connect(self.InsertTerritory)
        self.ui.territory_delete_pushButton.clicked.connect(self.DeleteTerritory)

        self.ui.house_insert_pushButton.clicked.connect(self.InsertHouse)
        self.ui.house_delete_pushButton.clicked.connect(self.DeleteHouse)
        # 打字的長這樣
        self.ui.chracter_name_lineEdit.returnPressed.connect(self.DEF)
        self.ui.start_sql_button.clicked.connect(self.sqlCommand)
    def showUpdate(self, table):
        mycursor.execute(f"SELECT * FROM {table}")
        result = mycursor.fetchall()
        output = ""
        for data in result:
            output = output + str(data) + "\n"
        self.ui.sql_output_label.setText(output)
    def InsertCharacter(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.chracter_name_lineEdit.text()
        status = self.ui.chracter_status_lineEdit.text()
        try:
            marriage = int(self.ui.chracter_marriage_lineEdit.text())
        except:
            marriage = None
        house_id = int(self.ui.chracter_house_lineEdit.text())
        try:
            actor_id = int(self.ui.chracter_actor_lineEdit.text())
        except:
            actor_id = None
        sql = "INSERT INTO Characters (name, status, actor_id, marriage, house_id) VALUES (%s, %s, %s, %s, %s)"
        value = (name, status, actor_id, marriage, house_id)
        mycursor.execute(sql,value)
        db.commit()
        self.ui.chracter_actor_lineEdit.clear()
        self.ui.chracter_house_lineEdit.clear()
        self.ui.chracter_marriage_lineEdit.clear()
        self.ui.chracter_name_lineEdit.clear()
        self.ui.chracter_status_lineEdit.clear()
        sql = "INSERT INTO Characters (name, status, actor_id, marriage, house_id)\nVALUES\n("
        for data in value:
            sql = sql + str(data) + ","
        sql = sql[:-1]
        sql = sql + ")"
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.showUpdate("Characters")
        pass
    def DeleteCharacter(self):
        self.ui.sql_command_plainTextEdit.clear()
        sql = ""
        name = self.ui.chracter_name_lineEdit.text()
        name = "\"" + name + "\""
        sql = f"DELETE FROM Characters WHERE name = {name}"
        # print(name)
        if name == "\"\"":
            status = self.ui.chracter_status_lineEdit.text()
            status = "\'" + status + "\'"
            sql = f"DELETE FROM Characters WHERE status = {status}"
        try:
            marriage = int(self.ui.chracter_marriage_lineEdit.text())
            sql = f"DELETE FROM Characters WHERE marriage = {marriage}"
        except:
            pass
        try:
            house_id = int(self.ui.chracter_house_lineEdit.text())
            sql = f"DELETE FROM Characters WHERE house_id = {house_id}"
        except:
            pass
        try:
            actor_id = int(self.ui.chracter_actor_lineEdit.text())
            sql = f"DELETE FROM Characters WHERE actor_id = {actor_id}"
        except:
            pass
        print(sql)
        mycursor.execute(sql)
        db.commit()
        self.ui.chracter_actor_lineEdit.clear()
        self.ui.chracter_house_lineEdit.clear()
        self.ui.chracter_marriage_lineEdit.clear()
        self.ui.chracter_name_lineEdit.clear()
        self.ui.chracter_status_lineEdit.clear()
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.showUpdate("Characters")
    def InsertPlayer(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.player_name_lineEdit.text()
        country = self.ui.player_country_lineEdit.text()
        try:
            char_id = int(self.ui.player_character_lineEdit.text())
        except:
            char_id = None
        gender = self.ui.player_gender_lineEdit.text()
        sql = "INSERT INTO Players (name, country, char_id, gender) VALUES (%s, %s, %s, %s)"
        value = (name, country, char_id, gender)
        mycursor.execute(sql,value)
        db.commit()
        self.ui.player_name_lineEdit.clear()
        self.ui.player_gender_lineEdit.clear()
        self.ui.player_character_lineEdit.clear()
        self.ui.player_country_lineEdit.clear()
        sql = "INSERT INTO Players (name, country, char_id, gender)\nVALUES\n("
        for data in value:
            sql = sql + str(data) + ","
        sql = sql[:-1]
        sql = sql + ")"
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.showUpdate("Players")
        pass
    def DeletePlayer(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.player_name_lineEdit.text()
        country = self.ui.player_country_lineEdit.text()
        gender = self.ui.player_gender_lineEdit.text()
        try:
            char_id = int(self.ui.player_character_lineEdit.text())
        except:
            char_id = None
        if name != '':
            name = "\"" + name +"\""
            sql = f"DELETE FROM Players WHERE name = {name}"
        elif country != '':
            country = "\"" + country + "\""
            sql = f"DELETE FROM Players WHERE country = {country}"
        elif gender != '':
            gender =  "\"" + gender + "\""
            sql = f"DELETE FROM Players WHERE gender = {gender}"
        else:
            sql = f"DELETE FROM Players WHERE char_id = {char_id}"
        print(sql)
        mycursor.execute(sql)
        db.commit()
        self.ui.player_name_lineEdit.clear()
        self.ui.player_gender_lineEdit.clear()
        self.ui.player_character_lineEdit.clear()
        self.ui.player_country_lineEdit.clear()
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.showUpdate("Players")
        pass
    
    def InsertHouse(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.house_name_lineEdit.text()
        try:
            alliance = int(self.ui.house_alliance_lineEdit.text())
        except:
            alliance = None
        # try:
        #     ruler = int(self.ui.house_ruler_lineEdit.text())
        # except:
        #     ruler = None
        words = self.ui.house_ruler_lineEdit.text()
        sql = "INSERT INTO Houses (name, words, alliance_house_id) VALUES (%s, %s, %s)"
        value = (name, words, alliance)
        mycursor.execute(sql,value)
        db.commit()
        self.ui.house_name_lineEdit.clear()
        self.ui.house_ruler_lineEdit.clear()
        self.ui.house_alliance_lineEdit.clear()
        sql = "INSERT INTO Houses (name, words, alliance_house_id)\nVALUES\n("
        for data in value:
            sql = sql + str(data) + ","
        sql = sql[:-1]
        sql = sql + ")"
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.showUpdate("Houses")
        pass
    def DeleteHouse(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.house_name_lineEdit.text()
        try:
            alliance = int(self.ui.house_alliance_lineEdit.text())
        except:
            alliance = None
        try:
            ruler = int(self.ui.house_ruler_lineEdit.text())
        except:
            ruler = None
        
        if name != '':
            name = '\''+name+'\''
            sql = f"DELETE FROM Houses WHERE name = {name}"
        elif alliance != None:
            sql = f"DELETE FROM Houses WHERE alliance = {alliance}"
        else:
            sql = f"DELETE FROM Houses WHERE ruler = {ruler}"
        mycursor.execute(sql)
        db.commit()
        self.ui.house_name_lineEdit.clear()
        self.ui.house_ruler_lineEdit.clear()
        self.ui.house_alliance_lineEdit.clear()
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.showUpdate("Houses")
        pass

    def InsertWar(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.war_name_lineEdit.text()
        place_id = int(self.ui.war_place_lineEdit.text())
        p1 = int(self.ui.war_participants_lineEdit_1.text())
        p2 = int(self.ui.war_participants_lineEdit_2.text())
        try:
            p3 = int(self.ui.war_participants_lineEdit_3.text())
        except:
            p3 = None
        try:
            p4 = int(self.ui.war_participants_lineEdit_4.text())
        except:
            p4 = None
        sql = "INSERT INTO Wars (war_name, participant1_id, participant2_id, participant3_id, participant4_id, place_id) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (name, p1, p2, p3 ,p4 , place_id)
        mycursor.execute(sql,value)
        db.commit()
        self.ui.war_name_lineEdit.clear()
        self.ui.war_participants_lineEdit_1.clear()
        self.ui.war_participants_lineEdit_2.clear()
        self.ui.war_participants_lineEdit_3.clear()
        self.ui.war_participants_lineEdit_4.clear()
        self.ui.war_place_lineEdit.clear()
        sql = "INSERT INTO Wars (war_name, participant1_id, participant2_id, participant3_id, participant4_id, place_id)\nVALUES\n("
        for data in value:
            sql = sql + str(data) + ","
        sql = sql[:-1]
        sql = sql + ")"
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.showUpdate("Wars")
        pass
    def DeleteWar(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.war_name_lineEdit.text()
        place_id = int(self.ui.war_place_lineEdit.text())
        if name != '':
            name = '\'' + name + '\''
            sql = f"DELETE FROM Wars WHERE name = {name}"
        else:
            sql = f"DELETE FROM Wars WHERE name = {place_id}"
        mycursor.execute(sql)
        db.commit()
        self.ui.war_name_lineEdit.clear()
        self.ui.war_participants_lineEdit_1.clear()
        self.ui.war_participants_lineEdit_2.clear()
        self.ui.war_participants_lineEdit_3.clear()
        self.ui.war_participants_lineEdit_4.clear()
        self.ui.war_place_lineEdit.clear()
        self.showUpdate("Wars")
        pass

    def InsertTerritory(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.territory_name_lineEdit.text()
        try:
            ruler = int(self.ui.territory_ruler_lineEdit.text())
        except:
            ruler = None
        try:
            house = int(self.ui.territory_house_lineEdit.text())
        except:
            house = None
        sql = "INSERT INTO Territories (name, ruler_id, house_id) VALUES (%s, %s, %s)"
        value = (name, ruler, house)
        mycursor.execute(sql,value)
        db.commit()
        self.ui.house_name_lineEdit.clear()
        self.ui.house_ruler_lineEdit.clear()
        self.ui.house_alliance_lineEdit.clear()
        sql = "INSERT INTO Territories (name, ruler_id, house_id)\nVALUES\n("
        for data in value:
            sql = sql + str(data) + ","
        sql = sql[:-1]
        sql = sql + ")"
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.ui.territory_name_lineEdit.clear()
        self.ui.territory_house_lineEdit.clear()
        self.ui.territory_ruler_lineEdit.clear()
        self.showUpdate("Territories")
        pass
    def DeleteTerritory(self):
        self.ui.sql_command_plainTextEdit.clear()
        name = self.ui.territory_name_lineEdit.text()
        try:
            ruler = int(self.ui.territory_ruler_lineEdit.text())
        except:
            ruler = None
        try:
            house = int(self.ui.territory_house_lineEdit.text())
        except:
            house = None
        if name != '':
            name = "\'" + name + "\'"
            sql = f"DELETE FROM Territories WHERE name = {name}"
        elif ruler != None:
            sql = f"DELETE FROM Territories WHERE ruler_id = {ruler}"
        else:
            sql = f"DELETE FROM Territories WHERE house_id = {house}"
        mycursor.execute(sql)
        db.commit()
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
        self.ui.territory_name_lineEdit.clear()
        self.ui.territory_house_lineEdit.clear()
        self.ui.territory_ruler_lineEdit.clear()
        self.showUpdate("Territories")
        pass
    def sqlCommand(self):
        sql = self.ui.sql_command_plainTextEdit.toPlainText()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        output = ""
        for data in result:
            output = output + str(data) + "\n"
        self.ui.sql_output_label.setText(output)
    """
    SELECT * FROM Characters
    SELECT-FROM-WHERE : SELECT name FROM Characters WHERE status = 'Alive'
    DELETE : DELETE FROM Characters WHERE name = 'demo2'
    INSERT : 
    INSERT INTO Characters (name, status, actor_id, marriage, house_id)
VALUES
('demo2','Alive',999,999,999)
    UPDATE : 
        UPDATE Territories SET ruler_id=50 WHERE territory_id=8;
        SELECT * FROM Territories;
    IN : SELECT name FROM Characters WHERE house_id IN ( SELECT name FROM Players WHERE gender = 'Female')
    NOT IN : SELECT name FROM Characters WHERE house_id IN ( SELECT name FROM Players WHERE gender = 'Female')
    EXISTS : 
    SELECT name FROM Characters WHERE EXISTS ( SELECT * FROM Houses WHERE Characters.house_id = Houses.house_id AND Houses.house_id = 0)
    NOT EXISTS : 
    SELECT name FROM Territories WHERE NOT EXISTS ( SELECT * FROM Wars WHERE Wars.place_id = Territories.territory_id)
    COUNT : SELECT COUNT(*) FROM Characters GROUP BY house_id
    SUM : SELECT SUM(age) FROM Players
    MAX : SELECT MAX(age) FROM Players
    MIN : SELECT MIN(age) FROM Players
    AVG : SELECT AVG(age) FROM Players
    HAVING : SELECT country FROM Players GROUP BY country HAVING COUNT(*) > 0
    """
    def Button(self):
        Act = self.ui.comboBox.currentText()
        self.ui.sql_command_plainTextEdit.clear()
        sql = ""
        meaning = ""
        if Act == "SELECT":
            meaning = "印出所有存活的角色\n"
            sql = "SELECT name FROM Characters WHERE status = \'Alive\'"
        elif Act == "UPDATE":
            meaning = "把territory_id為8的ruler_id更新成50\n"
            sql = "UPDATE Territories SET ruler_id=50 WHERE territory_id=8;"
        elif Act == "IN":
            meaning = "印出女性角色\n"
            sql = "SELECT name FROM Characters WHERE actor_id IN ( SELECT actor_id FROM Players WHERE gender = \'Female\')"
        elif Act == "NOT IN":
            meaning = "印出男性角色\n"
            sql = "SELECT name FROM Characters WHERE actor_id NOT IN ( SELECT actor_id FROM Players WHERE gender = \'Female\')"
        elif Act == "EXISTS":
            meaning = "印出house_id為０的角色\n"
            sql = "SELECT name FROM Characters WHERE EXISTS ( SELECT * FROM Houses WHERE Characters.house_id = Houses.house_id AND Houses.house_id = 0)"
        elif Act == "NOT EXISTS":
            meaning = "沒有發生過戰爭的地區\n"
            sql = "SELECT name FROM Territories WHERE NOT EXISTS ( SELECT * FROM Wars WHERE Wars.place_id = Territories.territory_id)"
        elif Act == "COUNT":
            meaning = "印出每個house有幾個人\n"
            sql = "SELECT COUNT(*) FROM Characters GROUP BY house_id"
        elif Act == "SUM":
            meaning = "印出演員的年齡加總\n"
            sql = "SELECT SUM(age) FROM Players"
        elif Act == "MAX":
            meaning = "印出最老的演員年齡\n"
            sql = "SELECT MAX(age) FROM Players"
        elif Act == "MIN":
            meaning = "印出最年輕的演員年齡\n"
            sql = "SELECT MIN(age) FROM Players"
        elif Act == "AVG":
            meaning = "印出演員平均年齡\n"
            sql = "SELECT AVG(age) FROM Players"
        elif Act == "HAVING":
            meaning = "超過兩個演員來自的國家\n"
            sql = "SELECT country FROM Players GROUP BY country HAVING COUNT(*) > 1"
        if Act == "UPDATE":
            mycursor.execute(sql)
            self.showUpdate("Territories")
            sql = sql + "\nSELECT * FROM Territories"
        else:
            mycursor.execute(sql)
            result = mycursor.fetchall()
            output = ""
            for data in result:
                output = output + str(data) + "\n"
            self.ui.sql_output_label.setText(output)
        sql = meaning + sql
        self.ui.sql_command_plainTextEdit.insertPlainText(sql)
    def DEF(self):
        pass