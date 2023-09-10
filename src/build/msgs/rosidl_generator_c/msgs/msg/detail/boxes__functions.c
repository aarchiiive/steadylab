// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from msgs:msg/Boxes.idl
// generated code does not contain a copyright notice
#include "msgs/msg/detail/boxes__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
msgs__msg__Boxes__init(msgs__msg__Boxes * msg)
{
  if (!msg) {
    return false;
  }
  // a
  return true;
}

void
msgs__msg__Boxes__fini(msgs__msg__Boxes * msg)
{
  if (!msg) {
    return;
  }
  // a
}

bool
msgs__msg__Boxes__are_equal(const msgs__msg__Boxes * lhs, const msgs__msg__Boxes * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // a
  if (lhs->a != rhs->a) {
    return false;
  }
  return true;
}

bool
msgs__msg__Boxes__copy(
  const msgs__msg__Boxes * input,
  msgs__msg__Boxes * output)
{
  if (!input || !output) {
    return false;
  }
  // a
  output->a = input->a;
  return true;
}

msgs__msg__Boxes *
msgs__msg__Boxes__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msgs__msg__Boxes * msg = (msgs__msg__Boxes *)allocator.allocate(sizeof(msgs__msg__Boxes), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(msgs__msg__Boxes));
  bool success = msgs__msg__Boxes__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
msgs__msg__Boxes__destroy(msgs__msg__Boxes * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    msgs__msg__Boxes__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
msgs__msg__Boxes__Sequence__init(msgs__msg__Boxes__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msgs__msg__Boxes * data = NULL;

  if (size) {
    data = (msgs__msg__Boxes *)allocator.zero_allocate(size, sizeof(msgs__msg__Boxes), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = msgs__msg__Boxes__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        msgs__msg__Boxes__fini(&data[i - 1]);
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
msgs__msg__Boxes__Sequence__fini(msgs__msg__Boxes__Sequence * array)
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
      msgs__msg__Boxes__fini(&array->data[i]);
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

msgs__msg__Boxes__Sequence *
msgs__msg__Boxes__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  msgs__msg__Boxes__Sequence * array = (msgs__msg__Boxes__Sequence *)allocator.allocate(sizeof(msgs__msg__Boxes__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = msgs__msg__Boxes__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
msgs__msg__Boxes__Sequence__destroy(msgs__msg__Boxes__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    msgs__msg__Boxes__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
msgs__msg__Boxes__Sequence__are_equal(const msgs__msg__Boxes__Sequence * lhs, const msgs__msg__Boxes__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!msgs__msg__Boxes__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
msgs__msg__Boxes__Sequence__copy(
  const msgs__msg__Boxes__Sequence * input,
  msgs__msg__Boxes__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(msgs__msg__Boxes);
    msgs__msg__Boxes * data =
      (msgs__msg__Boxes *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!msgs__msg__Boxes__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          msgs__msg__Boxes__fini(&data[i]);
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
    if (!msgs__msg__Boxes__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
