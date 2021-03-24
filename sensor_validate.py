spike_threshold_limit         = {
                                  'soc'      :  0.05 ,
                                  'current'  :  0.1  ,
                                }

def isAbnormalSpike(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def hasAbnormalSpike(values,criteria):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not isAbnormalSpike(values[i], values[i + 1], spike_threshold_limit[criteria])):
      return True
  return False

def isValidValueList(values):
    if isinstance(values, list) and len(values) != 0:
        return True
    return False

def isValidReading(values,criteria):
    if isValidValueList(values) and not hasAbnormalSpike(values,criteria):
        return True
    return False
