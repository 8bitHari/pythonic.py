def main():
    spacecraft = [
        {"name": "Voyager 1", "distance": 163},
        {"name": "James Webb Space Telescope"}
    ]
    
    print(create_report(spacecraft))
    

def create_report(spacecraft):
    report = "=========== REPORT ===========\n\n"
    for s in spacecraft:
        report += f"Name: {s['name']}\n"
        report += f"Distance: {s.get('distance', 'Unknown')} AU\n\n"
    report += "=============================="
    return report

main()