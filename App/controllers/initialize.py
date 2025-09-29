from App.database import db
from App.models import Admin, Driver, Resident, Area, Street


def initialize():
    db.drop_all()
    db.create_all()

    #Creating Admin
    admin = Admin(username="admin", password="adminpass")
    db.session.add(admin)
    db.session.commit()

    #Creating Areas and Streets
    area1 = Area(name='St. Augustine')
    db.session.add(area1)
    db.session.commit()

    street11 = Street(name="Gordon Street", areaId=area1.id)
    street12 = Street(name="Warner Street", areaId=area1.id)
    street13 = Street(name="College Road", areaId=area1.id)
    db.session.add_all([street11, street12, street13])
    db.session.commit()

    area2 = Area(name='Tunapuna')
    db.session.add(area2)
    db.session.commit()

    street21 = Street(name="Fairly Street", areaId=area2.id)
    street22 = Street(name="Saint John Road", areaId=area2.id)
    db.session.add_all([street21, street22])
    db.session.commit()

    area3 = Area(name='San Juan')
    db.session.add(area3)
    db.session.commit()

    #Creating Drivers
    driver1 = Driver(username="bob",
                     password="bobpass",
                     status="Offline",
                     areaId=area1.id,
                     streetId=street11.id)
    driver2 = Driver(username="mary",
                     password="marypass",
                     status="Available",
                     areaId=area2.id,
                     streetId=None)
    db.session.add_all([driver1, driver2])
    db.session.commit()

    #Creating Residents and Stops
    resident1 = Resident(username="alice",
                         password="alicepass",
                         areaId=area1.id,
                         streetId=street12.id,
                         houseNumber=48)
    resident2 = Resident(username="jane",
                         password="janepass",
                         areaId=area1.id,
                         streetId=street12.id,
                         houseNumber=50)
    resident3 = Resident(username="john",
                         password="johnpass",
                         areaId=area2.id,
                         streetId=street21.id,
                         houseNumber=13)
    db.session.add_all([resident1, resident2, resident3])
    db.session.commit()

    #Creating Drives and Stops
    driver2.schedule_drive(area1.id, street12.id, "2025-10-26", "10:00")
    db.session.commit()
                     
    resident2.request_stop(0)
    db.session.commit()
