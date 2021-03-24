import unittest
import sensor_validate

class SensorValidatorTest(unittest.TestCase):
  def test_reports_error_when_soc_jumps(self):
    self.assertFalse(
      sensor_validate.validate_reading([0.0, 0.01, 0.5, 'soc'])
    )
  
  def test_reports_error_when_current_jumps(self):
    self.assertFalse(
      sensor_validate.validate_reading([0.03, 0.03, 0.03, 'current'])
    )

if __name__ == "__main__":
  unittest.main()
