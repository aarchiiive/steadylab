// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from serial_communication:msg/ReadCar.idl
// generated code does not contain a copyright notice
#include "serial_communication/msg/detail/read_car__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
serial_communication__msg__ReadCar__init(serial_communication__msg__ReadCar * msg)
{
  if (!msg) {
    return false;
  }
  // read_aorm
  // read_e_stop
  // read_gear
  // read_speed
  // read_brake
  // read_enc
  // read_steer
  // read_s
  // read_l
  // read_yaw
  // read_velocity
  // read_accel
  return true;
}

void
serial_communication__msg__ReadCar__fini(serial_communication__msg__ReadCar * msg)
{
  if (!msg) {
    return;
  }
  // read_aorm
  // read_e_stop
  // read_gear
  // read_speed
  // read_brake
  // read_enc
  // read_steer
  // read_s
  // read_l
  // read_yaw
  // read_velocity
  // read_accel
}

bool
serial_communication__msg__ReadCar__are_equal(const serial_communication__msg__ReadCar * lhs, const serial_communication__msg__ReadCar * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // read_aorm
  if (lhs->read_aorm != rhs->read_aorm) {
    return false;
  }
  // read_e_stop
  if (lhs->read_e_stop != rhs->read_e_stop) {
    return false;
  }
  // read_gear
  if (lhs->read_gear != rhs->read_gear) {
    return false;
  }
  // read_speed
  if (lhs->read_speed != rhs->read_speed) {
    return false;
  }
  // read_brake
  if (lhs->read_brake != rhs->read_brake) {
    return false;
  }
  // read_enc
  if (lhs->read_enc != rhs->read_enc) {
    return false;
  }
  // read_steer
  if (lhs->read_steer != rhs->read_steer) {
    return false;
  }
  // read_s
  if (lhs->read_s != rhs->read_s) {
    return false;
  }
  // read_l
  if (lhs->read_l != rhs->read_l) {
    return false;
  }
  // read_yaw
  if (lhs->read_yaw != rhs->read_yaw) {
    return false;
  }
  // read_velocity
  if (lhs->read_velocity != rhs->read_velocity) {
    return false;
  }
  // read_accel
  if (lhs->read_accel != rhs->read_accel) {
    return false;
  }
  return true;
}

bool
serial_communication__msg__ReadCar__copy(
  const serial_communication__msg__ReadCar * input,
  serial_communication__msg__ReadCar * output)
{
  if (!input || !output) {
    return false;
  }
  // read_aorm
  output->read_aorm = input->read_aorm;
  // read_e_stop
  output->read_e_stop = input->read_e_stop;
  // read_gear
  output->read_gear = input->read_gear;
  // read_speed
  output->read_speed = input->read_speed;
  // read_brake
  output->read_brake = input->read_brake;
  // read_enc
  output->read_enc = input->read_enc;
  // read_steer
  output->read_steer = input->read_steer;
  // read_s
  output->read_s = input->read_s;
  // read_l
  output->read_l = input->read_l;
  // read_yaw
  output->read_yaw = input->read_yaw;
  // read_velocity
  output->read_velocity = input->read_velocity;
  // read_accel
  output->read_accel = input->read_accel;
  return true;
}

serial_communication__msg__ReadCar *
serial_communication__msg__ReadCar__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serial_communication__msg__ReadCar * msg = (serial_communication__msg__ReadCar *)allocator.allocate(sizeof(serial_communication__msg__ReadCar), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(serial_communication__msg__ReadCar));
  bool success = serial_communication__msg__ReadCar__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
serial_communication__msg__ReadCar__destroy(serial_communication__msg__ReadCar * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    serial_communication__msg__ReadCar__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
serial_communication__msg__ReadCar__Sequence__init(serial_communication__msg__ReadCar__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serial_communication__msg__ReadCar * data = NULL;

  if (size) {
    data = (serial_communication__msg__ReadCar *)allocator.zero_allocate(size, sizeof(serial_communication__msg__ReadCar), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = serial_communication__msg__ReadCar__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        serial_communication__msg__ReadCar__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
serial_communication__msg__ReadCar__Sequence__fini(serial_communication__msg__ReadCar__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      serial_communication__msg__ReadCar__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

serial_communication__msg__ReadCar__Sequence *
serial_communication__msg__ReadCar__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serial_communication__msg__ReadCar__Sequence * array = (serial_communication__msg__ReadCar__Sequence *)allocator.allocate(sizeof(serial_communication__msg__ReadCar__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = serial_communication__msg__ReadCar__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
serial_communication__msg__ReadCar__Sequence__destroy(serial_communication__msg__ReadCar__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    serial_communication__msg__ReadCar__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
serial_communication__msg__ReadCar__Sequence__are_equal(const serial_communication__msg__ReadCar__Sequence * lhs, const serial_communication__msg__ReadCar__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!serial_communication__msg__ReadCar__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
serial_communication__msg__ReadCar__Sequence__copy(
  const serial_communication__msg__ReadCar__Sequence * input,
  serial_communication__msg__ReadCar__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(serial_communication__msg__ReadCar);
    serial_communication__msg__ReadCar * data =
      (serial_communication__msg__ReadCar *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!serial_communication__msg__ReadCar__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          serial_communication__msg__ReadCar__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!serial_communication__msg__ReadCar__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
