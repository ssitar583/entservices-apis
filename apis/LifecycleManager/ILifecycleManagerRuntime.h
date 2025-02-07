/*
 * If not stated otherwise in this file or this component's LICENSE file the
 * following copyright and licenses apply:
 *
 * Copyright 2024 RDK Management
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once

#include "Module.h"

namespace WPEFramework {
namespace Exchange {
struct EXTERNAL ILifecycleManagerRuntime : virtual public Core::IUnknown {

    enum AppTerminatedReason : uint8_t {
	REQUESTED,
	CRASHED,
	SELF_TERMINATED
    };

    enum { ID = ID_LIFECYCLE_MANAGER_RUNTIME };

    /**  notification API call in response to terminateRuntime */
    //  @json:omit
    // @brief  notification API call in response to terminateRuntime
    virtual Core::hresult RuntimeTerminated(const string& appInstanceId /* @in */, const AppTerminatedReason terminatedReason /* @in */) { return Core::ERROR_NONE; };

};
} // namespace Exchange
} // namespace WPEFramework
