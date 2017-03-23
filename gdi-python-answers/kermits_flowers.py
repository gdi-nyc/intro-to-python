def willKermitPlantFlowers(day, season, currentTemperature):
    if day.lower() == 'saturday' and season.lower() == 'spring' and currentTemperature > 65:
        print "Kermit will plant some flowers today!"
    else:
        print "Kermit cannot plant flowers today, maybe tomorrow"

# will plant flowers
willKermitPlantFlowers('Saturday', 'Spring', 70)

# will not plant flowers
willKermitPlantFlowers('Saturday', 'Fall', 75)
