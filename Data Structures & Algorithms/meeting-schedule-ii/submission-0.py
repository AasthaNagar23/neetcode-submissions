"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s=[]
        e=[]
        for meeting in intervals:
            s.append(meeting.start)
            e.append(meeting.end)
        s.sort()
        e.sort()
        i=0
        j=0
        room=0
        max_room=0
        while i<len(s):
            if s[i]<e[j]:
                room+=1
                max_room=max(room,max_room)
                i+=1
            else:
                room-=1
                j+=1
        return max_room