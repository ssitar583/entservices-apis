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

// @stubgen:include <com/IIteratorType.h>

namespace WPEFramework {
namespace Exchange {
// @text:keep
struct EXTERNAL IRuntimeManager : virtual public Core::IUnknown {

    enum { ID = ID_RUNTIME_MANAGER };

    using IStringIterator = RPC::IIteratorType<string, RPC::ID_STRINGITERATOR>;
    using IValueIterator = RPC::IIteratorType<uint32_t, RPC::ID_VALUEITERATOR>;

    // @event 
    struct EXTERNAL INotification : virtual public Core::IUnknown
    {
        enum { ID = ID_RUNTIME_MANAGER_NOTIFICATION };
 
        // @brief Notifies container is started
        // @text onStarted
        // @json:omit
        virtual void OnStarted(const string& appInstanceId) {};
 
        // @brief Notifies container is shutdown
        // @text onTerminated
        // @json:omit
        virtual void OnTerminated(const string& appInstanceId) {};
 
        // @brief Notifies failure in container execution
        // @text onFailure
        // @json:omit
        virtual void OnFailure(const string& appInstanceId, const string& error) {};
 
        // @brief Notifies state of container
        // @text onStateChanged
        // @json:omit
        virtual void OnStateChanged(const string& appInstanceId, const string& state) {};
        // Possible state values {Starting, running, suspended, hibernating, hibernated, waking, terminating, terminated}
    };

    /** Register notification interface */
    virtual Core::hresult Register(INotification *notification) = 0;

    /** Unregister notification interface */
    virtual Core::hresult Unregister(INotification *notification) = 0;

    /** Run the application */
    // @json:omit
    // @text run
    virtual Core::hresult Run(const string& appInstanceId /* @in */, const string& appPath /* @in */, const string& runtimePath /* @in */, IStringIterator* const& envVars /* @in */, const uint32_t userId /* @in */, const uint32_t groupId /* @in */, IValueIterator* const& ports /* @in */, IStringIterator* const& paths /* @in */, IStringIterator* const& debugSettings /* @in */, bool& success /* @out */) = 0;

    /** Hibernate the application */
    // @json:omit
    // @text hibernate
    virtual Core::hresult Hibernate(const string& appInstanceId /* @in */, bool& success /* @out */) const = 0;

    /** Wake the application to given state */
    // @json:omit
    // @text wake
    virtual Core::hresult Wake(const string& appInstanceId /* @in */, const string& state /* @in */, bool& success /* @out */) const = 0;

    /** Suspend the application */
    // @json:omit
    // @text suspend
    virtual Core::hresult Suspend(const string& appInstanceId /* @in */, bool& success /* @out */) const = 0;

    /** Resume the application */
    // @json:omit
    // @text resume
    virtual Core::hresult Resume(const string& appInstanceId /* @in */, bool& success /* @out */) const = 0;

    /** Terminate the application */
    // @json:omit
    // @text terminate
    virtual Core::hresult Terminate(const string& appInstanceId /* @in */, bool& success /* @out */) const = 0;

    /** Kill the application */
    // @json:omit
    // @text kill
    virtual Core::hresult Kill(const string& appInstanceId /* @in */, bool& success /* @out */) const = 0;

    /** get info of the application */
    // @json:omit
    // @text getInfo
    virtual Core::hresult GetInfo(const string& appInstanceId /* @in */, const string& info /* @in */, bool& success /* @out */) const = 0;

    // @json:omit
    // @text annotate
    virtual Core::hresult Annotate(const string& appInstanceId /* @in */, const string& key /* @in */, const string& value /* @in */, bool& success /* @out */) const = 0;

    // @json:omit
    // @text mount
    virtual Core::hresult Mount() const = 0;

    // @json:omit
    // @text unmount
    virtual Core::hresult Unmount() const = 0;
};
} // namespace Exchange
} // namespace WPEFramework
