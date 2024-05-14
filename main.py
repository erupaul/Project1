from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapMarker

from opencage.geocoder import OpenCageGeocode

class BusinessAddressGeolocationApp(App):
    def build(self):
        self.title = "Business Address Geolocation Finder"
        
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Enter the business address to get its geolocation:")
        layout.add_widget(label)
        
        self.address_input = TextInput(hint_text="Business Address")
        layout.add_widget(self.address_input)
        
        button = Button(text="Get Geolocation")
        button.bind(on_press=self.get_geolocation)
        layout.add_widget(button)
        
        self.result_label = Label()
        layout.add_widget(self.result_label)
        
        self.map_view = MapView(zoom=15)
        layout.add_widget(self.map_view)
        
        return layout
    
    def get_geolocation(self, instance):
        business_address = self.address_input.text
        api_key = "b66f4a212b474ecda2d411bd918252de"
        
        geocoder = OpenCageGeocode(api_key)
        result = geocoder.geocode(business_address)

        if result and 'geometry' in result[0]:
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']
            
            self.result_label.text = "Geolocation found:\nLatitude: {}\nLongitude: {}".format(lat, lng)
            
            self.map_view.center_on(lat, lng)
            marker = MapMarker(lat=lat, lon=lng)
            self.map_view.add_marker(marker)
        else:
            self.result_label.text = "Geolocation not found for the given business address."

if __name__ == "__main__":
    BusinessAddressGeolocationApp().run()