import unittest
import sensor_validate

class SensorValidatorTest(unittest.TestCase):
  def test_error_when_soc_jumps(self):
    self.assertFalse(
      sensor_validate.isValidReading([0.0, 0.01, 0.5, 0.51],'soc')
    )
    
  def test_error_when_no_readings(self):
    self.assertFalse(
      sensor_validate.isValidReading([],'soc')
    )
    
  def test_error_when_sensor_off(self):
    self.assertFalse(
      sensor_validate.isValidReading(None,'soc')
    )
    
  def test_noerror_when_soc_readings_OK(self):
    self.assertTrue(
      sensor_validate.isValidReading([0.0, 0.01, 0.02, 0.03],'soc')
    )
    
  def test_noerror_when_current_readings_OK(self):
    self.assertTrue(
      sensor_validate.isValidReading([0.03, 0.03, 0.03, 0.03],'current')
    )
  
  def test_error_when_current_jumps(self):
    self.assertFalse(
      sensor_validate.isValidReading([0.03, 0.03, 0.03, 0.33],'current')
    )

if __name__ == "__main__":
  unittest.main()
