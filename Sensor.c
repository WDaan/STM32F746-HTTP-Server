#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "cmsis_os2.h"
#include <math.h>
#include "Driver_I2C.h"
#include "Sensor.h"
#include "Board_GLCD.h"                 // ::Board Support:Graphic LCD
#include "stm32f7xx_hal.h"
#include "Board_LED.h"

#define TEMP_I2C_ADDR    0x48            /* 7-bit I2C address                  */

/* I2C driver instance */
extern ARM_DRIVER_I2C            Driver_I2C1;
static ARM_DRIVER_I2C *I2Cdrv = &Driver_I2C1;

uint8_t wanted_temperature = 20;

uint8_t TC74_read () {
  uint8_t data;
	uint8_t val;

  data = 0;
  I2Cdrv->MasterTransmit(TEMP_I2C_ADDR, &data, 1, true);
  while (I2Cdrv->GetStatus().busy);
  if (I2Cdrv->GetDataCount() != 1) return -1;
  I2Cdrv->MasterReceive (TEMP_I2C_ADDR, &val, 1, false);
  while (I2Cdrv->GetStatus().busy);
  if (I2Cdrv->GetDataCount() != 1) return -1;

  return val;
}

void TC74_Initialize (){
  I2Cdrv->Initialize (NULL);

	I2Cdrv->PowerControl (ARM_POWER_FULL);
	I2Cdrv->Control (ARM_I2C_BUS_SPEED, ARM_I2C_BUS_SPEED_STANDARD);
	I2Cdrv->Control (ARM_I2C_BUS_CLEAR,0);
}

/* get fanstate */
uint8_t * get_fanstate(uint8_t currTemp){
	if(currTemp > wanted_temperature){
			LED_On(0);
		return "ON";
	}
		LED_Off(0);
	return "OFF";
}

void display_data(void){
	  char    buf[24];
	  uint32_t x = 5;
	 /* Display user text lines */
		uint8_t temp = TC74_read();
		sprintf (buf, "Fan status: %s  ", get_fanstate(temp));
    GLCD_DrawString (x*16U, 7U*24U, buf);
		
		
    sprintf (buf, "Temperature: %d C  ", temp != NULL ? temp: 0);
    GLCD_DrawString (x*16U, 8U*24U, buf);
}