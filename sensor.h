#include "stm32f7xx_hal.h" 
void TC74_Initialize (void);
uint8_t TC74_read(void);
uint8_t * get_fanstate(uint8_t, uint8_t);
void display_data(void);