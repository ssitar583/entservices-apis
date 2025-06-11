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

namespace WPEFramework
{
    namespace Exchange
    {
        // @json @text:keep
        struct EXTERNAL IFrontPanel : virtual public Core::IUnknown {
            enum { ID = ID_HDMI_CEC_SOURCE };


            struct EXTERNAL FrontPanelSuccess {
                bool success;
            };

            using IFrontPanelLightsListIterator = RPC::IIteratorType<string, ID_FRONT_PANEL_LIGHTS_LIST_ITERATOR>;



            // @json:omit
            virtual Core::hresult Register(Exchange::IFrontPanel::INotification *notification) = 0;
            // @json:omit
            virtual Core::hresult Unregister(Exchange::IFrontPanel::INotification *notification) = 0;
            // @json:omit
            virtual Core::hresult Configure(PluginHost::IShell* service) = 0;

            // @brief Gets the status of the Front Panel
            // @text getBrightness
            // @param index: Index of the brightness level
            // @param brightness: Brightness level
            // @param success: Is the operation successful or not
            virtual Core::hresult GetBrightness(string &index /* @in */, int32_t brightness /* out */, bool &success /* @out */) = 0;

            // @brief Gets the clock brightness of the Front Panel
            // @text getClockBrightness
            // @param brightness: Brightness level of the clock
            // @param success: Is the operation successful or not
            virtual Core::hresult GetClockBrightness(uint32_t &brightness /* @out */, bool &success /* @out */) = 0;

            // @brief Gets the front panel lights
            // @text getFrontPanelLights
            // @param supportedLights: List of supported front panel lights
            // @param supportedLightsInfo: Information about the supported front panel lights
            virtual Core::hresult getFrontPanelLights(IFrontPanelLightsListIterator &supportedLights /* @out */, string &supportedLightsInfo /* @out */) = 0;

            


        };
} // namespace Exchange
} // namespace WPEFramework
