//
//  FirstViewController.swift
//  Homely
//
//  Created by wei yi on 23/08/2016.
//  Copyright © 2016 wei yi. All rights reserved.
//

import UIKit
import GoogleMaps
import Foundation
import Alamofire

class FirstViewController: UIViewController {
    
    let locationManager = CLLocationManager()
    
    @IBOutlet weak var mapView: GMSMapView!
    override func viewDidLoad() {
        //locationManager.delegate = self
        //locationManager.requestWhenInUseAuthorization()
        super.viewDidLoad()
        
        mapView.camera = GMSCameraPosition.camera(withLatitude: -34.9297759, longitude: 138.5979703, zoom: 13.5)
        

//        Alamofire.request("http://127.0.0.1:5000/shorttime").responseJSON { response in
//            print(response.request)  // original URL request
//            print(response.response) // HTTP URL response
//            print(response.data)     // server data
//            print(response.result)   // result of response serialization
//            
//            
//            if let JSON = response.result.value {
//                //print("JSON: \(JSON)")
//                for item in JSON as! [Dictionary<String, AnyObject>]{
//                    
//                    self.addMarker(lat:Float(item["lat"] as! Float), lng:Float(item["lng"] as! Float), title: item["primecontrol"] as! String, type: 1)
//                    //print(item["zid"])
//                }
//            }
//        }
        
//        Alamofire.request("http://127.0.0.1:5000/2hr").responseJSON { response in
//            print(response.request)  // original URL request
//            print(response.response) // HTTP URL response
//            print(response.data)     // server data
//            print(response.result)   // result of response serialization
//            
//            
//            if let JSON = response.result.value {
//                //print("JSON: \(JSON)")
//                for item in JSON as! [Dictionary<String, AnyObject>]{
//                    
//                    self.addMarker(lat:Float(item["lat"] as! Float), lng:Float(item["lng"] as! Float), title: item["primecontrol"] as! String, type: 2)
//                    //print(item["zid"])
//                }
//            }
//        }
        
        Alamofire.request("http://127.0.0.1:5000/3hr").responseJSON { response in
            print(response.request)  // original URL request
            print(response.response) // HTTP URL response
            print(response.data)     // server data
            print(response.result)   // result of response serialization
            
            
            if let JSON = response.result.value {
                //print("JSON: \(JSON)")
                for item in JSON as! [Dictionary<String, AnyObject>]{
                    
                    self.addMarker(lat:Float(item["lat"] as! Float), lng:Float(item["lng"] as! Float), title: item["primecontrol"] as! String, type: 3)
                    //print(item["zid"])
                }
            }
        }
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }

   
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    func addMarker(lat: Float, lng: Float, title: String, type: Int) {
        let marker = GMSMarker()
        marker.position = CLLocationCoordinate2D(latitude: CLLocationDegrees(lat), longitude: CLLocationDegrees(lng))
        marker.title = title
        marker.snippet = "Australia"
        marker.map = mapView
        if(type == 1){
            marker.icon = GMSMarker.markerImage(with: UIColor.red)
        }else if(type == 2){
            marker.icon = GMSMarker.markerImage(with: UIColor.orange)
        }else if(type == 3){
            marker.icon = GMSMarker.markerImage(with: UIColor.blue)
        }
    }
}

extension FirstViewController: CLLocationManagerDelegate {
    // 2
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        // 3
        if status == .authorizedWhenInUse {
            
            // 4
            locationManager.startUpdatingLocation()
            
            //5
            mapView.isMyLocationEnabled = true
            mapView.settings.myLocationButton = true
        }
    }
    
    // 6
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.first {
            
            // 7
            mapView.camera = GMSCameraPosition(target: location.coordinate, zoom: 15, bearing: 0, viewingAngle: 0)
            
            // 8
            locationManager.stopUpdatingLocation()
        }
        
    }
}


