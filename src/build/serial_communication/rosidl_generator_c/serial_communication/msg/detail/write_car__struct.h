// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from serial_communication:msg/WriteCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__STRUCT_H_
#define SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/WriteCar in the package serial_communication.
typedef struct serial_communication__msg__WriteCar
{
  bool write_e_stop;
  int8_t write_gear;
  int16_t write_speed;
  int16_t write_brake;
  int32_t write_steer;
} serial_communication__msg__WriteCar;

// Struct for a sequence of serial_communication__msg__WriteCar.
typedef struct serial_communication__msg__WriteCar__Sequence
{
  serial_communication__msg__WriteCar * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} serial_communication__msg__WriteCar__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__STRUCT_H_
