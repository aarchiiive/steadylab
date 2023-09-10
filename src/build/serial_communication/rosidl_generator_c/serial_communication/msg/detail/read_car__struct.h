// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from serial_communication:msg/ReadCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__STRUCT_H_
#define SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ReadCar in the package serial_communication.
typedef struct serial_communication__msg__ReadCar
{
  bool read_aorm;
  bool read_e_stop;
  int8_t read_gear;
  int16_t read_speed;
  int16_t read_brake;
  int64_t read_enc;
  int32_t read_steer;
  double read_s;
  double read_l;
  double read_yaw;
  double read_velocity;
  double read_accel;
} serial_communication__msg__ReadCar;

// Struct for a sequence of serial_communication__msg__ReadCar.
typedef struct serial_communication__msg__ReadCar__Sequence
{
  serial_communication__msg__ReadCar * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} serial_communication__msg__ReadCar__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__READ_CAR__STRUCT_H_
