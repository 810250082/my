from start import *

db.create_all()

# page1 = Page(1 , 1)
# page2 = Page(2 , 2)
# tag1 = Tag(1 , 'good')
# tag2 = Tag(2 , 'bad')
# tags1 = db.Tages()
# page1 = Page(3 , 3)
# page2 = Page(4 , 4)
# tag1 = Tag(3 , 'small')
# tag2 = Tag(4 , 'cool')
# db.session.add(page1)
# db.session.add(page2)
# db.session.add(tag1)
# db.session.add(tag2)
# db.session.commit()

tag = Tag.query.filter_by(name='bad').first()
print(tag)


