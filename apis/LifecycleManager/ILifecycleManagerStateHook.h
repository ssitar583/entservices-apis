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
#include "ILifecycleManager.h"
// @stubgen:include "ILifecycleManager.h"

namespace WPEFramework {
namespace Exchange {

struct EXTERNAL ILifecycleManagerStateHook : virtual public Core::IUnknown {

    enum { ID = ID_LIFECYCLE_MANAGER_STATE_HOOK };

    /** Notifies about application becaming active */
    // @json:omit
    // @param appInstanceId: application instance id
    // @param appId: application id
    // @param appPath: application path
    // @param loadParameters: string containing JSON formated information about how to communicate with Ripple
    // @brief Notifies about application becaming active
    virtual Core::hresult AppInitializing(const string& appInstanceId /* @in */,
                                        const string& appId /* @in */,
                                        const string& appPath /* @in */,
                                        string& loadParameters /* @out */) = 0;

    /** Notifies about state change */
    // @json:omit
    // @param appInstanceId: application instance id
    // @param oldLifecycleState: old application state
    // @param newLifecycleState: new application state
    // @param navigationIntent: optional intent string, should be set when newLifecycleState is active_requested
    // @param stateChangeId: monotonic state change id
    // @param activeSessionId: optional active session id
    // @brief Notifies about state change
    virtual Core::hresult AppLifecycleStateChanged(const string& appInstanceId /* @in */,
                                                const ILifecycleManager::LifecycleState oldLifecycleState /* @in */,
                                                const ILifecycleManager::LifecycleState newLifecycleState /* @in */,
                                                const string& navigationIntent /* @in */,
                                                const uint32_t stateChangeId /* @in */,
                                                const bool activeSessionId /* @in */) = 0;

};
} // namespace Exchange
} // namespace WPEFramework
