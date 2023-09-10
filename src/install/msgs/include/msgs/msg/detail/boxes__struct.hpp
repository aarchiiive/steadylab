// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from msgs:msg/Boxes.idl
// generated code does not contain a copyright notice

#ifndef MSGS__MSG__DETAIL__BOXES__STRUCT_HPP_
#define MSGS__MSG__DETAIL__BOXES__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__msgs__msg__Boxes __attribute__((deprecated))
#else
# define DEPRECATED__msgs__msg__Boxes __declspec(deprecated)
#endif

namespace msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Boxes_
{
  using Type = Boxes_<ContainerAllocator>;

  explicit Boxes_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0ll;
    }
  }

  explicit Boxes_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0ll;
    }
  }

  // field types and members
  using _a_type =
    int64_t;
  _a_type a;

  // setters for named parameter idiom
  Type & set__a(
    const int64_t & _arg)
  {
    this->a = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msgs::msg::Boxes_<ContainerAllocator> *;
  using ConstRawPtr =
    const msgs::msg::Boxes_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msgs::msg::Boxes_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msgs::msg::Boxes_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msgs::msg::Boxes_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msgs::msg::Boxes_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msgs::msg::Boxes_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msgs::msg::Boxes_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msgs::msg::Boxes_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msgs::msg::Boxes_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msgs__msg__Boxes
    std::shared_ptr<msgs::msg::Boxes_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msgs__msg__Boxes
    std::shared_ptr<msgs::msg::Boxes_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Boxes_ & other) const
  {
    if (this->a != other.a) {
      return false;
    }
    return true;
  }
  bool operator!=(const Boxes_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Boxes_

// alias to use template instance with default allocator
using Boxes =
  msgs::msg::Boxes_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace msgs

#endif  // MSGS__MSG__DETAIL__BOXES__STRUCT_HPP_
