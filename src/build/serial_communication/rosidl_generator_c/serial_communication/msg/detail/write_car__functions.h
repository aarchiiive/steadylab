// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from serial_communication:msg/WriteCar.idl
// generated code does not contain a copyright notice

#ifndef SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__FUNCTIONS_H_
#define SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "serial_communication/msg/rosidl_generator_c__visibility_control.h"

#include "serial_communication/msg/detail/write_car__struct.h"

/// Initialize msg/WriteCar message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * serial_communication__msg__WriteCar
 * )) before or use
 * serial_communication__msg__WriteCar__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
bool
serial_communication__msg__WriteCar__init(serial_communication__msg__WriteCar * msg);

/// Finalize msg/WriteCar message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
void
serial_communication__msg__WriteCar__fini(serial_communication__msg__WriteCar * msg);

/// Create msg/WriteCar message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * serial_communication__msg__WriteCar__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
serial_communication__msg__WriteCar *
serial_communication__msg__WriteCar__create();

/// Destroy msg/WriteCar message.
/**
 * It calls
 * serial_communication__msg__WriteCar__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
void
serial_communication__msg__WriteCar__destroy(serial_communication__msg__WriteCar * msg);

/// Check for msg/WriteCar message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
bool
serial_communication__msg__WriteCar__are_equal(const serial_communication__msg__WriteCar * lhs, const serial_communication__msg__WriteCar * rhs);

/// Copy a msg/WriteCar message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
bool
serial_communication__msg__WriteCar__copy(
  const serial_communication__msg__WriteCar * input,
  serial_communication__msg__WriteCar * output);

/// Initialize array of msg/WriteCar messages.
/**
 * It allocates the memory for the number of elements and calls
 * serial_communication__msg__WriteCar__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
bool
serial_communication__msg__WriteCar__Sequence__init(serial_communication__msg__WriteCar__Sequence * array, size_t size);

/// Finalize array of msg/WriteCar messages.
/**
 * It calls
 * serial_communication__msg__WriteCar__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
void
serial_communication__msg__WriteCar__Sequence__fini(serial_communication__msg__WriteCar__Sequence * array);

/// Create array of msg/WriteCar messages.
/**
 * It allocates the memory for the array and calls
 * serial_communication__msg__WriteCar__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
serial_communication__msg__WriteCar__Sequence *
serial_communication__msg__WriteCar__Sequence__create(size_t size);

/// Destroy array of msg/WriteCar messages.
/**
 * It calls
 * serial_communication__msg__WriteCar__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
void
serial_communication__msg__WriteCar__Sequence__destroy(serial_communication__msg__WriteCar__Sequence * array);

/// Check for msg/WriteCar message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
bool
serial_communication__msg__WriteCar__Sequence__are_equal(const serial_communication__msg__WriteCar__Sequence * lhs, const serial_communication__msg__WriteCar__Sequence * rhs);

/// Copy an array of msg/WriteCar messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_serial_communication
bool
serial_communication__msg__WriteCar__Sequence__copy(
  const serial_communication__msg__WriteCar__Sequence * input,
  serial_communication__msg__WriteCar__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SERIAL_COMMUNICATION__MSG__DETAIL__WRITE_CAR__FUNCTIONS_H_
