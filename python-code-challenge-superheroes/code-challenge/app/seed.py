from models import Hero, HeroPower, Power, db
from app  import app
from random import choice as rc

with app.app_context():
  Hero.query.delete()
  HeroPower.query.delete()
  Power.query.delete()
#puts "🦸‍♀️ Seeding powers..."
  powers = [
  { 'name': "super strength", 'description': "gives the wielder super-human strengths" },
    { 'name': "flight", 'description': "gives the wielder the ability to fly through the skies at supersonic speed" },
    { 'name': "super human senses", 'description': "allows the wielder to use her senses at a super-human level" },
    { 'name': "elasticity", 'description': "can stretch the human body to extreme lengths" }
  ]
  for data in powers:
        power = Power(**data)
        db.session.add(power)

        db.session.commit()

# #puts "🦸‍♀️ Seeding heroes..."
  heroes = [
    { 'name': "Kamala Khan", 'super_name': "Ms. Marvel" },
    { 'name': "Doreen Green", 'super_name': "Squirrel Girl" },
    { 'name': "Gwen Stacy", 'super_name': "Spider-Gwen" },
    { 'name': "Janet Van Dyne", 'super_name': "The Wasp" },
    { 'name': "Wanda Maximoff", 'super_name': "Scarlet Witch" },
    { 'name': "Carol Danvers", 'super_name': "Captain Marvel" },
    { 'name': "Jean Grey", 'super_name': "Dark Phoenix" },
    { 'name': "Ororo Munroe", 'super_name': "Storm" },
    { 'name': "Kitty Pryde", 'super_name': "Shadowcat" },
    { 'name': "Elektra Natchios", 'super_name': "Elektra" }
  ]

  for data in heroes:
          hero = Hero(**data)
          db.session.add(hero)

          db.session.commit()

# #puts "🦸‍♀️ Adding powers to heroes..."

  strengths = ["Strong", "Weak", "Average"]
  
  all_heroes_power = Hero.query.all()
  all_power = Power.query.all()
  # heroes_power =  ["ddd", "bbb"]
  hero_power = []
  
  # for n in range (6):
  for hero in heroes :
    power= rc(all_power)
    heroes_power= rc(all_heroes_power)
    power_item = HeroPower(strength = rc(strengths),  hero_id=heroes_power.id, power_id=power.id)
    hero_power.append(power_item)

  db.session.add_all(hero_power)
  db.session.commit() 
  #
  print (power)
  
  # Hero.all.each do |hero|
  #   rand(1..3).times do
  #     # get a random power
  #     power = Power.find(Power.pluck(:id).sample)

  #     HeroPower.create!(hero_id: hero.id, power_id: power.id, strength: strengths.sample)
  #   end
  # end 

# #puts "🦸‍♀️ Done seeding!"
