// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from serial_communication:msg/WriteCar.idl
// generated code does not contain a copyright notice
#include "serial_communication/msg/detail/write_car__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
serial_communication__msg__WriteCar__init(serial_communication__msg__WriteCar * msg)
{
  if (!msg) {
    return false;
  }
  // write_e_stop
  // write_gear
  // write_speed
  // write_brake
  // write_steer
  return true;
}

void
serial_communication__msg__WriteCar__fini(serial_communication__msg__WriteCar * msg)
{
  if (!msg) {
    return;
  }
  // write_e_stop
  // write_gear
  // write_speed
  // write_brake
  // write_steer
}

bool
serial_communication__msg__WriteCar__are_equal(const serial_communication__msg__WriteCar * lhs, const serial_communication__msg__WriteCar * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // write_e_stop
  if (lhs->write_e_stop != rhs->write_e_stop) {
    return false;
  }
  // write_gear
  if (lhs->write_gear != rhs->write_gear) {
    return false;
  }
  // write_speed
  if (lhs->write_speed != rhs->write_speed) {
    return false;
  }
  // write_brake
  if (lhs->write_brake != rhs->write_brake) {
    return false;
  }
  // write_steer
  if (lhs->write_steer != rhs->write_steer) {
    return false;
  }
  return true;
}

bool
serial_communication__msg__WriteCar__copy(
  const serial_communication__msg__WriteCar * input,
  serial_communication__msg__WriteCar * output)
{
  if (!input || !output) {
    return false;
  }
  // write_e_stop
  output->write_e_stop = input->write_e_stop;
  // write_gear
  output->write_gear = input->write_gear;
  // write_speed
  output->write_speed = input->write_speed;
  // write_brake
  output->write_brake = input->write_brake;
  // write_steer
  output->write_steer = input->write_steer;
  return true;
}

serial_communication__msg__WriteCar *
serial_communication__msg__WriteCar__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serial_communication__msg__WriteCar * msg = (serial_communication__msg__WriteCar *)allocator.allocate(sizeof(serial_communication__msg__WriteCar), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(serial_communication__msg__WriteCar));
  bool success = serial_communication__msg__WriteCar__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
serial_communication__msg__WriteCar__destroy(serial_communication__msg__WriteCar * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    serial_communication__msg__WriteCar__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
serial_communication__msg__WriteCar__Sequence__init(serial_communication__msg__WriteCar__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serial_communication__msg__WriteCar * data = NULL;

  if (size) {
    data = (serial_communication__msg__WriteCar *)allocator.zero_allocate(size, sizeof(serial_communication__msg__WriteCar), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = serial_communication__msg__WriteCar__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        serial_communication__msg__WriteCar__fini(&data[i - 1]);
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
serial_communication__msg__WriteCar__Sequence__fini(serial_communication__msg__WriteCar__Sequence * array)
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
      serial_communication__msg__WriteCar__fini(&array->data[i]);
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

serial_communication__msg__WriteCar__Sequence *
serial_communication__msg__WriteCar__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  serial_communication__msg__WriteCar__Sequence * array = (serial_communication__msg__WriteCar__Sequence *)allocator.allocate(sizeof(serial_communication__msg__WriteCar__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = serial_communication__msg__WriteCar__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
serial_communication__msg__WriteCar__Sequence__destroy(serial_communication__msg__WriteCar__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    serial_communication__msg__WriteCar__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
serial_communication__msg__WriteCar__Sequence__are_equal(const serial_communication__msg__WriteCar__Sequence * lhs, const serial_communication__msg__WriteCar__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!serial_communication__msg__WriteCar__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
serial_communication__msg__WriteCar__Sequence__copy(
  const serial_communication__msg__WriteCar__Sequence * input,
  serial_communication__msg__WriteCar__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(serial_communication__msg__WriteCar);
    serial_communication__msg__WriteCar * data =
      (serial_communication__msg__WriteCar *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!serial_communication__msg__WriteCar__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          serial_communication__msg__WriteCar__fini(&data[i]);
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
    if (!serial_communication__msg__WriteCar__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
